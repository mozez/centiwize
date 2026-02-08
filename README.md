# Centiwize - Energy ROI Calculator

A web application to help Dutch homeowners calculate potential savings from energy improvements.

## Features

- **Address Lookup**: Auto-fill property data from official BAG register
- **Energy Usage Input**: Three methods (simple, annual, detailed)
- **7 Energy Improvements**: Calculate ROI for each upgrade
- **Detailed Analysis**: Payback period, lifetime savings, CO2 reduction

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python FastAPI
- **Hosting**: Vercel (serverless)
- **Data Sources**: Kadaster BAG API, PDOK

## Deployment to Vercel

### 1. Install Vercel CLI

```bash
npm install -g vercel
```

### 2. Login to Vercel

```bash
vercel login
```

### 3. Deploy

```bash
cd centiwize
vercel
```

### 4. Set Environment Variables

Go to your Vercel dashboard → Project Settings → Environment Variables and add:

| Variable | Description |
|----------|-------------|
| `KADASTER_API_KEY` | Your Kadaster BAG API key (get free at [kadaster.nl](https://www.kadaster.nl/zakelijk/producten/adressen-en-gebouwen/bag-api-individuele-bevragingen)) |

### 5. Redeploy

```bash
vercel --prod
```

## Local Development

### Prerequisites

- Python 3.9+
- pip

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variable
export KADASTER_API_KEY="your-api-key"  # Optional

# Run server
uvicorn api.index:app --reload
```

Open http://localhost:8000 in your browser.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info |
| `/api/health` | GET | Health check |
| `/api/lookup` | GET | Address lookup |

### Address Lookup Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `postcode` | Yes | Dutch postal code (e.g., 1012AB) |
| `huisnummer` | Yes | House number |
| `toevoeging` | No | House number addition (e.g., A, bis) |

### Example

```bash
curl "https://your-app.vercel.app/api/lookup?postcode=1012AB&huisnummer=1"
```

## Project Structure

```
centiwize/
├── api/
│   └── index.py          # FastAPI backend
├── public/
│   └── index.html        # Frontend
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── README.md
```

## Data Sources

- **Kadaster BAG API**: Official building register (floor area, build year)
- **PDOK Locatieserver**: Fallback for address validation

## Author

Mosesdot

## License

MIT
