from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import httpx
import os

app = FastAPI(title="Centiwize Energy ROI API")

# Email configuration (using Resend)
RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = os.environ.get("FROM_EMAIL", "noreply@centiwize.com")
BUSINESS_PHONE = os.environ.get("BUSINESS_PHONE", "+31612345678")

# Supabase configuration (public keys only - safe to expose)
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY", "")

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
    email_configured: bool


class EmailReportRequest(BaseModel):
    email: str
    name: str = "Homeowner"
    address: Optional[str] = None
    area: Optional[str] = None
    volume: Optional[str] = None
    annualSavings: Optional[int] = None
    totalInvestment: Optional[int] = None
    paybackYears: Optional[str] = None
    lifetimeSavings: Optional[int] = None
    co2Reduction: Optional[int] = None
    improvements: Optional[List[str]] = None


class EmailReportResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    error: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Centiwize Energy ROI API", "docs": "/docs"}


@app.get("/api/config")
async def get_config():
    """Return public configuration for the frontend"""
    return {
        "supabase_url": SUPABASE_URL,
        "supabase_anon_key": SUPABASE_ANON_KEY,
        "business_phone": BUSINESS_PHONE
    }


@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        kadaster_configured=bool(KADASTER_API_KEY),
        email_configured=bool(RESEND_API_KEY)
    )


def build_improvements_html(improvements):
    """Build HTML for improvements list"""
    if not improvements:
        return ""
    items = "".join(f"<li>{imp}</li>" for imp in improvements)
    return f"<div class='improvements'><strong>Selected Improvements:</strong><ul>{items}</ul></div>"


@app.post("/api/send-report", response_model=EmailReportResponse)
async def send_email_report(request: EmailReportRequest):
    """Send energy savings report via email"""

    if not RESEND_API_KEY:
        return EmailReportResponse(
            success=False,
            error="Email service not configured"
        )

    # Build conditional parts
    property_html = f'<p><strong>Property:</strong> {request.address}</p>' if request.address else ''
    area_html = f'<p><strong>Floor Area:</strong> {request.area} m² | <strong>Volume:</strong> {request.volume} m³</p>' if request.area else ''
    improvements_html = build_improvements_html(request.improvements)
    whatsapp_num = BUSINESS_PHONE.replace('+', '').replace(' ', '')

    annual_savings = request.annualSavings or 0
    total_investment = request.totalInvestment or 0
    lifetime_savings = request.lifetimeSavings or 0
    co2_reduction = request.co2Reduction or 0
    payback_years = request.paybackYears or '0'

    # Build email HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #1a5f2a 0%, #2d8f47 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
            .highlight {{ background: #e8f5e9; padding: 20px; border-radius: 8px; margin: 20px 0; }}
            .savings {{ font-size: 2.5em; color: #1a5f2a; font-weight: bold; }}
            .stat {{ display: inline-block; width: 45%; margin: 10px 2%; text-align: center; padding: 15px; background: white; border-radius: 8px; }}
            .stat-value {{ font-size: 1.5em; color: #1a5f2a; font-weight: bold; }}
            .stat-label {{ color: #666; font-size: 0.9em; }}
            .improvements {{ background: white; padding: 15px; border-radius: 8px; margin-top: 20px; }}
            .footer {{ text-align: center; margin-top: 30px; color: #666; font-size: 0.9em; }}
            .cta {{ display: inline-block; background: #25D366; color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Your Energy Savings Report</h1>
                <p>Centiwize Energy ROI Calculator</p>
            </div>
            <div class="content">
                <p>Hi {request.name},</p>
                <p>Thank you for using the Centiwize Energy Calculator. Here's your personalized energy savings report:</p>

                {property_html}
                {area_html}

                <div class="highlight">
                    <p style="margin: 0; text-align: center;">Estimated Annual Savings</p>
                    <p class="savings" style="text-align: center; margin: 10px 0;">€{annual_savings:,}</p>
                </div>

                <div style="text-align: center;">
                    <div class="stat">
                        <div class="stat-value">€{total_investment:,}</div>
                        <div class="stat-label">Total Investment</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{payback_years} years</div>
                        <div class="stat-label">Payback Period</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">€{lifetime_savings:,}</div>
                        <div class="stat-label">25-Year Savings</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{co2_reduction:,} kg</div>
                        <div class="stat-label">CO2 Reduction/Year</div>
                    </div>
                </div>

                {improvements_html}

                <div style="text-align: center; margin-top: 30px;">
                    <p>Ready to take the next step?</p>
                    <a href="https://wa.me/{whatsapp_num}?text=Hi! I received my Centiwize report and would like to discuss my options." class="cta">
                        Chat on WhatsApp
                    </a>
                </div>

                <div class="footer">
                    <p>This report was generated by Centiwize Energy ROI Calculator.</p>
                    <p>Calculations are estimates based on typical Dutch homes and may vary.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {RESEND_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "from": FROM_EMAIL,
                    "to": [request.email],
                    "subject": f"Your Energy Savings Report - €{request.annualSavings or 0:,}/year potential",
                    "html": html_content
                },
                timeout=10.0
            )

            if response.is_success:
                return EmailReportResponse(
                    success=True,
                    message="Report sent successfully"
                )
            else:
                error_data = response.json()
                return EmailReportResponse(
                    success=False,
                    error=error_data.get("message", "Failed to send email")
                )

    except Exception as e:
        return EmailReportResponse(
            success=False,
            error=str(e)
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
