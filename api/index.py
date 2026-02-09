from fastapi import FastAPI, HTTPException, Query, Request, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import httpx
import os
import json

app = FastAPI(title="Centiwize Energy ROI API")

# Configuration
RESEND_API_KEY = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL = os.environ.get("FROM_EMAIL", "noreply@centiwize.com")
BUSINESS_PHONE = os.environ.get("BUSINESS_PHONE", "+31612345678")
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY", "")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")
KADASTER_API_KEY = os.environ.get("KADASTER_API_KEY", "")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# REQUEST/RESPONSE MODELS
# ============================================

class AuthRequest(BaseModel):
    email: str
    password: str
    name: Optional[str] = None

class AuthResponse(BaseModel):
    success: bool
    user: Optional[Dict[str, Any]] = None
    session: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

class ProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None

class PropertyData(BaseModel):
    address: Optional[str] = None
    postal_code: Optional[str] = None
    house_number: Optional[str] = None
    area_m2: Optional[int] = None
    volume_m3: Optional[int] = None
    build_year: Optional[int] = None

class CalculationData(BaseModel):
    improvements: Optional[List[str]] = None
    annual_savings: Optional[float] = None
    total_investment: Optional[float] = None
    payback_years: Optional[float] = None
    lifetime_savings: Optional[float] = None
    co2_reduction: Optional[int] = None

class CalculationSave(BaseModel):
    property: Optional[PropertyData] = None
    calculation: CalculationData

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
    supabase_configured: bool

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

# ============================================
# HELPER FUNCTIONS
# ============================================

def get_supabase_headers(access_token: Optional[str] = None):
    """Get headers for Supabase API calls"""
    headers = {
        "apikey": SUPABASE_ANON_KEY,
        "Content-Type": "application/json"
    }
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    return headers

def get_service_headers():
    """Get headers for service-level Supabase access"""
    return {
        "apikey": SUPABASE_SERVICE_KEY or SUPABASE_ANON_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY or SUPABASE_ANON_KEY}",
        "Content-Type": "application/json"
    }

async def get_current_user(request: Request) -> Optional[Dict]:
    """Extract user from session cookie or auth header"""
    # Try to get token from cookie first
    token = request.cookies.get("access_token")

    # Fall back to Authorization header
    if not token:
        auth_header = request.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]

    if not token:
        return None

    # Verify token with Supabase
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{SUPABASE_URL}/auth/v1/user",
                headers={
                    "apikey": SUPABASE_ANON_KEY,
                    "Authorization": f"Bearer {token}"
                },
                timeout=10.0
            )
            if response.is_success:
                return response.json()
        except:
            pass
    return None

# ============================================
# BASIC ENDPOINTS
# ============================================

@app.get("/")
async def root():
    return {"message": "Centiwize Energy ROI API", "docs": "/docs"}

@app.get("/api/config")
async def get_config():
    """Return public configuration for the frontend"""
    return {
        "business_phone": BUSINESS_PHONE,
        "auth_enabled": bool(SUPABASE_URL and SUPABASE_ANON_KEY)
    }

@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        kadaster_configured=bool(KADASTER_API_KEY),
        email_configured=bool(RESEND_API_KEY),
        supabase_configured=bool(SUPABASE_URL and SUPABASE_ANON_KEY)
    )

# ============================================
# AUTHENTICATION ENDPOINTS
# ============================================

@app.post("/api/auth/register", response_model=AuthResponse)
async def register(request: AuthRequest, response: Response):
    """Register a new user"""
    if not SUPABASE_URL:
        return AuthResponse(success=False, error="Authentication not configured")

    async with httpx.AsyncClient() as client:
        try:
            result = await client.post(
                f"{SUPABASE_URL}/auth/v1/signup",
                headers=get_supabase_headers(),
                json={
                    "email": request.email,
                    "password": request.password,
                    "data": {"full_name": request.name} if request.name else {}
                },
                timeout=10.0
            )

            data = result.json()

            if result.status_code >= 400:
                return AuthResponse(
                    success=False,
                    error=data.get("msg") or data.get("error_description") or "Registration failed"
                )

            # Set session cookie if we have a session
            if data.get("access_token"):
                response.set_cookie(
                    key="access_token",
                    value=data["access_token"],
                    httponly=True,
                    secure=True,
                    samesite="lax",
                    max_age=3600
                )

            return AuthResponse(
                success=True,
                user=data.get("user"),
                session={"access_token": data.get("access_token")} if data.get("access_token") else None
            )

        except Exception as e:
            return AuthResponse(success=False, error=str(e))

@app.post("/api/auth/login", response_model=AuthResponse)
async def login(request: AuthRequest, response: Response):
    """Login user"""
    if not SUPABASE_URL:
        return AuthResponse(success=False, error="Authentication not configured")

    async with httpx.AsyncClient() as client:
        try:
            result = await client.post(
                f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
                headers=get_supabase_headers(),
                json={
                    "email": request.email,
                    "password": request.password
                },
                timeout=10.0
            )

            data = result.json()

            if result.status_code >= 400:
                return AuthResponse(
                    success=False,
                    error=data.get("msg") or data.get("error_description") or "Login failed"
                )

            # Set session cookie
            if data.get("access_token"):
                response.set_cookie(
                    key="access_token",
                    value=data["access_token"],
                    httponly=True,
                    secure=True,
                    samesite="lax",
                    max_age=data.get("expires_in", 3600)
                )
                response.set_cookie(
                    key="refresh_token",
                    value=data.get("refresh_token", ""),
                    httponly=True,
                    secure=True,
                    samesite="lax",
                    max_age=60*60*24*30  # 30 days
                )

            return AuthResponse(
                success=True,
                user=data.get("user"),
                session={"access_token": data.get("access_token")}
            )

        except Exception as e:
            return AuthResponse(success=False, error=str(e))

@app.post("/api/auth/logout")
async def logout(response: Response):
    """Logout user"""
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"success": True}

@app.get("/api/auth/session")
async def get_session(request: Request):
    """Get current session"""
    user = await get_current_user(request)
    if user:
        return {"success": True, "user": user}
    return {"success": False, "user": None}

@app.post("/api/auth/forgot-password")
async def forgot_password(email: str = Query(...)):
    """Send password reset email"""
    if not SUPABASE_URL:
        return {"success": False, "error": "Authentication not configured"}

    async with httpx.AsyncClient() as client:
        try:
            result = await client.post(
                f"{SUPABASE_URL}/auth/v1/recover",
                headers=get_supabase_headers(),
                json={"email": email},
                timeout=10.0
            )

            if result.status_code >= 400:
                data = result.json()
                return {"success": False, "error": data.get("msg", "Failed to send reset email")}

            return {"success": True, "message": "Password reset email sent"}

        except Exception as e:
            return {"success": False, "error": str(e)}

# ============================================
# PROFILE ENDPOINTS
# ============================================

@app.get("/api/profile")
async def get_profile(request: Request):
    """Get user profile"""
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = request.cookies.get("access_token") or request.headers.get("Authorization", "").replace("Bearer ", "")

    async with httpx.AsyncClient() as client:
        try:
            result = await client.get(
                f"{SUPABASE_URL}/rest/v1/profiles?id=eq.{user['id']}&select=*",
                headers={
                    **get_supabase_headers(token),
                    "Prefer": "return=representation"
                },
                timeout=10.0
            )

            data = result.json()
            if data and len(data) > 0:
                return {"success": True, "profile": data[0]}
            return {"success": True, "profile": None}

        except Exception as e:
            return {"success": False, "error": str(e)}

@app.put("/api/profile")
async def update_profile(profile: ProfileUpdate, request: Request):
    """Update user profile"""
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = request.cookies.get("access_token") or request.headers.get("Authorization", "").replace("Bearer ", "")

    update_data = {}
    if profile.full_name is not None:
        update_data["full_name"] = profile.full_name
    if profile.phone is not None:
        update_data["phone"] = profile.phone

    async with httpx.AsyncClient() as client:
        try:
            result = await client.patch(
                f"{SUPABASE_URL}/rest/v1/profiles?id=eq.{user['id']}",
                headers={
                    **get_supabase_headers(token),
                    "Prefer": "return=representation"
                },
                json=update_data,
                timeout=10.0
            )

            return {"success": True}

        except Exception as e:
            return {"success": False, "error": str(e)}

# ============================================
# CALCULATIONS ENDPOINTS
# ============================================

@app.get("/api/calculations")
async def get_calculations(request: Request):
    """Get user's saved calculations with property data"""
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = request.cookies.get("access_token") or request.headers.get("Authorization", "").replace("Bearer ", "")

    async with httpx.AsyncClient() as client:
        try:
            # Query with property join
            result = await client.get(
                f"{SUPABASE_URL}/rest/v1/calculations?user_id=eq.{user['id']}&select=*,properties(*)&order=created_at.desc",
                headers=get_supabase_headers(token),
                timeout=10.0
            )

            return {"success": True, "calculations": result.json()}

        except Exception as e:
            return {"success": False, "error": str(e)}

@app.post("/api/calculations")
async def save_calculation(calc: CalculationSave, request: Request):
    """Save a calculation with optional property data"""
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = request.cookies.get("access_token") or request.headers.get("Authorization", "").replace("Bearer ", "")

    async with httpx.AsyncClient() as client:
        try:
            property_id = None

            # If property data is provided, save/update property first
            if calc.property and calc.property.address:
                prop_result = await client.post(
                    f"{SUPABASE_URL}/rest/v1/properties",
                    headers={
                        **get_supabase_headers(token),
                        "Prefer": "return=representation,resolution=merge-duplicates"
                    },
                    json={
                        "user_id": user["id"],
                        "address": calc.property.address,
                        "postal_code": calc.property.postal_code or "",
                        "house_number": calc.property.house_number or "",
                        "area_m2": calc.property.area_m2,
                        "volume_m3": calc.property.volume_m3,
                        "build_year": calc.property.build_year
                    },
                    timeout=10.0
                )

                if prop_result.is_success:
                    prop_data = prop_result.json()
                    if prop_data and len(prop_data) > 0:
                        property_id = prop_data[0].get("id")

            # Save calculation
            calc_data = calc.calculation
            result = await client.post(
                f"{SUPABASE_URL}/rest/v1/calculations",
                headers={
                    **get_supabase_headers(token),
                    "Prefer": "return=representation"
                },
                json={
                    "user_id": user["id"],
                    "property_id": property_id,
                    "improvements": calc_data.improvements,
                    "annual_savings": calc_data.annual_savings,
                    "total_investment": calc_data.total_investment,
                    "payback_years": calc_data.payback_years,
                    "lifetime_savings": calc_data.lifetime_savings,
                    "co2_reduction": calc_data.co2_reduction
                },
                timeout=10.0
            )

            if result.status_code >= 400:
                return {"success": False, "error": "Failed to save calculation"}

            return {"success": True, "calculation": result.json()}

        except Exception as e:
            return {"success": False, "error": str(e)}

# ============================================
# NOTIFICATIONS ENDPOINTS
# ============================================

@app.get("/api/notifications")
async def get_notifications(request: Request):
    """Get user's notifications"""
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = request.cookies.get("access_token") or request.headers.get("Authorization", "").replace("Bearer ", "")

    async with httpx.AsyncClient() as client:
        try:
            result = await client.get(
                f"{SUPABASE_URL}/rest/v1/notifications?user_id=eq.{user['id']}&select=*&order=created_at.desc&limit=20",
                headers=get_supabase_headers(token),
                timeout=10.0
            )

            return {"success": True, "notifications": result.json()}

        except Exception as e:
            return {"success": False, "error": str(e)}

@app.put("/api/notifications/{notification_id}/read")
async def mark_notification_read(notification_id: str, request: Request):
    """Mark a notification as read"""
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = request.cookies.get("access_token") or request.headers.get("Authorization", "").replace("Bearer ", "")

    async with httpx.AsyncClient() as client:
        try:
            result = await client.patch(
                f"{SUPABASE_URL}/rest/v1/notifications?id=eq.{notification_id}&user_id=eq.{user['id']}",
                headers=get_supabase_headers(token),
                json={"read": True},
                timeout=10.0
            )

            return {"success": True}

        except Exception as e:
            return {"success": False, "error": str(e)}

# ============================================
# EMAIL ENDPOINT
# ============================================

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
        return EmailReportResponse(success=False, error="Email service not configured")

    property_html = f'<p><strong>Property:</strong> {request.address}</p>' if request.address else ''
    area_html = f'<p><strong>Floor Area:</strong> {request.area} m² | <strong>Volume:</strong> {request.volume} m³</p>' if request.area else ''
    improvements_html = build_improvements_html(request.improvements)
    whatsapp_num = BUSINESS_PHONE.replace('+', '').replace(' ', '')

    annual_savings = request.annualSavings or 0
    total_investment = request.totalInvestment or 0
    lifetime_savings = request.lifetimeSavings or 0
    co2_reduction = request.co2Reduction or 0
    payback_years = request.paybackYears or '0'

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
                <p>Thank you for using the Centiwize Energy Calculator.</p>
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
                </div>
                {improvements_html}
                <div style="text-align: center; margin-top: 30px;">
                    <a href="https://wa.me/{whatsapp_num}" class="cta">Chat on WhatsApp</a>
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
                    "subject": f"Your Energy Savings Report - €{annual_savings:,}/year",
                    "html": html_content
                },
                timeout=10.0
            )

            if response.is_success:
                return EmailReportResponse(success=True, message="Report sent!")
            else:
                return EmailReportResponse(success=False, error="Failed to send email")

    except Exception as e:
        return EmailReportResponse(success=False, error=str(e))

# ============================================
# ADDRESS LOOKUP ENDPOINTS
# ============================================

@app.get("/api/lookup", response_model=AddressLookupResponse)
async def lookup_address(
    postcode: str = Query(..., description="Dutch postal code"),
    huisnummer: str = Query(..., description="House number"),
    toevoeging: Optional[str] = Query(None, description="Addition")
):
    """Look up address details from BAG register"""
    postcode = postcode.replace(" ", "").upper()
    if len(postcode) != 6 or not postcode[:4].isdigit() or not postcode[4:].isalpha():
        raise HTTPException(status_code=400, detail="Invalid postal code format")

    if KADASTER_API_KEY:
        result = await lookup_kadaster(postcode, huisnummer, toevoeging)
        if result.success:
            return result

    return await lookup_pdok(postcode, huisnummer)


async def lookup_kadaster(postcode: str, huisnummer: str, toevoeging: Optional[str]) -> AddressLookupResponse:
    """Query Kadaster BAG API"""
    async with httpx.AsyncClient() as client:
        try:
            url = "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/adressen"
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
                return AddressLookupResponse(success=False, error="Invalid API key", source="kadaster")

            if response.status_code == 404 or not response.is_success:
                return AddressLookupResponse(success=False, error="Address not found", source="kadaster")

            data = response.json()
            if not data.get("_embedded", {}).get("adressen"):
                return AddressLookupResponse(success=False, error="Address not found", source="kadaster")

            address_data = data["_embedded"]["adressen"][0]
            full_address = (
                f"{address_data.get('openbareRuimteNaam', '')} "
                f"{address_data.get('huisnummer', '')}"
                f"{address_data.get('huisnummertoevoeging', '')}"
                f"{address_data.get('huisletter', '')}, "
                f"{address_data.get('postcode', '')} "
                f"{address_data.get('woonplaatsNaam', '')}"
            )

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
                    maakt_deel_uit_van = verblijfsobject.get("maaktDeelUitVan", [])
                    if maakt_deel_uit_van:
                        pand_id = maakt_deel_uit_van[0].get("identificatie")

            build_year = None
            if pand_id:
                pand_url = f"https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/panden/{pand_id}"
                pand_response = await client.get(pand_url, headers=headers, timeout=10.0)
                if pand_response.is_success:
                    pand_data = pand_response.json()
                    build_year = pand_data.get("pand", {}).get("oorspronkelijkBouwjaar")

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
            return AddressLookupResponse(success=False, error="Timeout", source="kadaster")
        except Exception as e:
            return AddressLookupResponse(success=False, error=str(e), source="kadaster")


async def lookup_pdok(postcode: str, huisnummer: str) -> AddressLookupResponse:
    """Fallback to PDOK"""
    async with httpx.AsyncClient() as client:
        try:
            query = f"{postcode} {huisnummer}"
            url = "https://api.pdok.nl/bzk/locatieserver/search/v3_1/free"
            params = {"q": query, "fq": "type:adres", "rows": 1}

            response = await client.get(url, params=params, timeout=10.0)
            data = response.json()

            docs = data.get("response", {}).get("docs", [])
            if not docs:
                return AddressLookupResponse(success=False, error="Address not found", source="pdok")

            address_data = docs[0]
            full_address = address_data.get("weergavenaam", "")
            area = address_data.get("oppervlakte")
            build_year = address_data.get("bouwjaar")

            estimated = False
            if not area:
                estimated = True
                pc_num = int(postcode[:4])
                if pc_num < 2000:
                    area = 95
                elif pc_num < 3000:
                    area = 110
                elif pc_num < 4000:
                    area = 115
                else:
                    area = 120

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
            return AddressLookupResponse(success=False, error=str(e), source="pdok")


def estimate_ceiling_height(build_year: Optional[int]) -> float:
    """Estimate ceiling height based on era"""
    if not build_year:
        return 2.6
    if build_year < 1945:
        return 3.0
    elif build_year < 1970:
        return 2.8
    elif build_year < 1990:
        return 2.5
    elif build_year < 2012:
        return 2.6
    else:
        return 2.7
