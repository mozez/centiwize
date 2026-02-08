from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import httpx
import os

app = FastAPI(title="Centiwize Energy ROI API")

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get API key from environment variable
KADASTER_API_KEY = os.environ.get("KADASTER_API_KEY", "")

# Response models
class AddressLookupResponse(BaseModel):
    success: bool
    address: Optional[str] = None
    area: Optional[int] = None
    volume: Optional[int] = None
    build_year: Optional[int] = None
    ceiling_height: Optional[float] = None
    estimated: bool = False
    source: str = "unknown"
    error: Optional[str] = None


class HealthResponse(BaseModel):
    status: str
    kadaster_configured: bool


@app.get("/")
async def root():
    return {"message": "Centiwize Energy ROI API", "docs": "/docs"}


@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        kadaster_configured=bool(KADASTER_API_KEY)
    )


@app.get("/api/lookup", response_model=AddressLookupResponse)
async def lookup_address(
    postcode: str = Query(..., description="Dutch postal code (e.g., 1012AB)"),
    huisnummer: str = Query(..., description="House number"),
    toevoeging: Optional[str] = Query(None, description="House number addition (e.g., A, bis)")
):
    """
    Look up address details from the official Dutch BAG register.
    Returns floor area, volume, and build year.
    """
    # Clean and validate postal code
    postcode = postcode.replace(" ", "").upper()
    if len(postcode) != 6 or not postcode[:4].isdigit() or not postcode[4:].isalpha():
        raise HTTPException(status_code=400, detail="Invalid postal code format. Use: 1234AB")

    # Try Kadaster BAG API first (if key is configured)
    if KADASTER_API_KEY:
        result = await lookup_kadaster(postcode, huisnummer, toevoeging)
        if result.success:
            return result

    # Fallback to PDOK
    return await lookup_pdok(postcode, huisnummer)


async def lookup_kadaster(postcode: str, huisnummer: str, toevoeging: Optional[str]) -> AddressLookupResponse:
    """Query the official Kadaster BAG API"""
    async with httpx.AsyncClient() as client:
        try:
            # Step 1: Look up address
            url = f"https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/adressen"
            params = {"postcode": postcode, "huisnummer": huisnummer}
            if toevoeging:
                params["huisnummertoevoeging"] = toevoeging

            headers = {
                "X-Api-Key": KADASTER_API_KEY,
                "Accept": "application/hal+json",
                "Accept-Crs": "epsg:28992"
            }

            response = await client.get(url, params=params, headers=headers, timeout=10.0)

            if response.status_code == 401:
                return AddressLookupResponse(
                    success=False,
                    error="Invalid Kadaster API key",
                    source="kadaster"
                )

            if response.status_code == 404 or not response.is_success:
                return AddressLookupResponse(
                    success=False,
                    error="Address not found in BAG register",
                    source="kadaster"
                )

            data = response.json()

            if not data.get("_embedded", {}).get("adressen"):
                return AddressLookupResponse(
                    success=False,
                    error="Address not found",
                    source="kadaster"
                )

            address_data = data["_embedded"]["adressen"][0]
            full_address = (
                f"{address_data.get('openbareRuimteNaam', '')} "
                f"{address_data.get('huisnummer', '')}"
                f"{address_data.get('huisnummertoevoeging', '')}"
                f"{address_data.get('huisletter', '')}, "
                f"{address_data.get('postcode', '')} "
                f"{address_data.get('woonplaatsNaam', '')}"
            )

            # Step 2: Get verblijfsobject (for floor area)
            adresseerbaar_object_id = address_data.get("adresseerbaarObjectIdentificatie")
            area = None
            pand_id = None

            if adresseerbaar_object_id:
                vo_url = f"https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/verblijfsobjecten/{adresseerbaar_object_id}"
                vo_response = await client.get(vo_url, headers=headers, timeout=10.0)

                if vo_response.is_success:
                    vo_data = vo_response.json()
                    verblijfsobject = vo_data.get("verblijfsobject", {})
                    area = verblijfsobject.get("oppervlakte")

                    # Get pand ID for build year
                    maakt_deel_uit_van = verblijfsobject.get("maaktDeelUitVan", [])
                    if maakt_deel_uit_van:
                        pand_id = maakt_deel_uit_van[0].get("identificatie")

            # Step 3: Get pand (for build year)
            build_year = None
            if pand_id:
                pand_url = f"https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/panden/{pand_id}"
                pand_response = await client.get(pand_url, headers=headers, timeout=10.0)

                if pand_response.is_success:
                    pand_data = pand_response.json()
                    build_year = pand_data.get("pand", {}).get("oorspronkelijkBouwjaar")

            # Calculate volume based on ceiling height (varies by era)
            ceiling_height = estimate_ceiling_height(build_year)
            volume = round(area * ceiling_height) if area else None

            return AddressLookupResponse(
                success=True,
                address=full_address.strip(),
                area=area,
                volume=volume,
                build_year=build_year,
                ceiling_height=ceiling_height,
                estimated=False,
                source="kadaster"
            )

        except httpx.TimeoutException:
            return AddressLookupResponse(
                success=False,
                error="Kadaster API timeout",
                source="kadaster"
            )
        except Exception as e:
            return AddressLookupResponse(
                success=False,
                error=str(e),
                source="kadaster"
            )


async def lookup_pdok(postcode: str, huisnummer: str) -> AddressLookupResponse:
    """Fallback to PDOK Locatieserver (free, no API key needed)"""
    async with httpx.AsyncClient() as client:
        try:
            query = f"{postcode} {huisnummer}"
            url = "https://api.pdok.nl/bzk/locatieserver/search/v3_1/free"
            params = {"q": query, "fq": "type:adres", "rows": 1}

            response = await client.get(url, params=params, timeout=10.0)
            data = response.json()

            docs = data.get("response", {}).get("docs", [])
            if not docs:
                return AddressLookupResponse(
                    success=False,
                    error="Address not found",
                    source="pdok"
                )

            address_data = docs[0]
            full_address = address_data.get("weergavenaam", "")

            # PDOK may have some data
            area = address_data.get("oppervlakte")
            build_year = address_data.get("bouwjaar")

            # Estimate area if not available based on region
            estimated = False
            if not area:
                estimated = True
                pc_num = int(postcode[:4])
                if pc_num < 2000:
                    area = 95  # Amsterdam region
                elif pc_num < 3000:
                    area = 110  # Rotterdam/Den Haag
                elif pc_num < 4000:
                    area = 115  # Utrecht region
                else:
                    area = 120  # Other regions

            ceiling_height = estimate_ceiling_height(build_year)
            volume = round(area * ceiling_height) if area else None

            return AddressLookupResponse(
                success=True,
                address=full_address,
                area=area,
                volume=volume,
                build_year=build_year,
                ceiling_height=ceiling_height,
                estimated=estimated,
                source="pdok"
            )

        except Exception as e:
            return AddressLookupResponse(
                success=False,
                error=str(e),
                source="pdok"
            )


def estimate_ceiling_height(build_year: Optional[int]) -> float:
    """Estimate ceiling height based on construction era"""
    if not build_year:
        return 2.6  # default
    if build_year < 1945:
        return 3.0
    elif build_year < 1970:
        return 2.8
    elif build_year < 1990:
        return 2.5
    elif build_year < 2012:
        return 2.6
    else:
        return 2.7  # newer buildings tend to have slightly higher ceilings


# For Vercel serverless
handler = app
