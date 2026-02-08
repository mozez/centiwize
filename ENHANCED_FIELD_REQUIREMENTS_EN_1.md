# Energy ROI Calculator - Enhanced Field Requirements
## Netherlands Edition - English Version

---

## REQUIRED FIELDS ✳️ (Must be filled for calculation)

### 1. Square Meters (m²)
- **Why Required**: Base measurement for floor area calculations
- **Input Type**: Number (positive integer)
- **Typical Range**: 50-300 m² for Dutch homes
- **Example**: 100 m²
- **Used For**: 
  - Estimating heating/cooling load
  - Insulation material calculations
  - Solar panel capacity planning
- **Default**: None - must be entered

---

### 2. Total Volume (m³) ✳️
- **Why Required**: Critical for accurate heating/cooling energy calculations
- **Input Type**: Number (positive decimal)
- **Calculation**: Floor area (m²) × ceiling height (m)
- **Typical Ceiling Heights**:
  - Standard modern home: 2.6m
  - Older homes: 2.4-2.8m
  - High ceilings: 3.0-3.5m
- **Examples**:
  - 100 m² × 2.6m = 260 m³
  - 150 m² × 2.5m = 375 m³
- **Used For**: 
  - HVAC sizing and efficiency calculations
  - Heat pump capacity determination
  - Ventilation requirements
  - More accurate heating cost estimates
- **Why It Matters**: Two homes with same floor area but different ceiling heights need different heating energy
- **Default**: Auto-calculated as (Square Meters × 2.5) if left blank
- **Manual Entry**: Recommended for accuracy

---

### 3. Energy Usage Data - CHOOSE ONE METHOD:

You must provide energy cost data using ONE of these three methods:

#### METHOD A: Simple Monthly Average (Easiest) ✳️
**Required if using this method:**

##### 3A-1. Average Monthly Electric Bill (€)
- **Input Type**: Euro amount
- **How to Calculate**: Sum of 12 months ÷ 12
- **Example**: €120/month
- **Where to Find**: Annual statement total ÷ 12

##### 3A-2. Average Monthly Gas Bill (€)
- **Input Type**: Euro amount (or €0 for all-electric)
- **How to Calculate**: Sum of 12 months ÷ 12
- **Example**: €150/month
- **Important**: Must be TRUE average, not just winter month
- **Where to Find**: Annual statement total ÷ 12

---

#### METHOD B: Annual Statement (More Accurate) ✳️
**Required if using this method:**

##### 3B-1. Total Annual Electric Cost (€)
- **Input Type**: Euro amount
- **Example**: €1,440/year (€120/month average)
- **Where to Find**: "Totaal Elektriciteit" on annual statement
- **Should Include**: 
  - Variable energy costs
  - Transport costs
  - Energy tax (ODE)
  - VAT (BTW)

##### 3B-2. Total Annual Gas Cost (€)
- **Input Type**: Euro amount (or €0 for all-electric)
- **Example**: €1,800/year (€150/month average)
- **Where to Find**: "Totaal Aardgas" on annual statement
- **Should Include**:
  - Variable energy costs
  - Transport costs
  - Energy tax
  - VAT (BTW)

---

#### METHOD C: Detailed Monthly Data (Most Accurate) ✳️
**Required if using this method:**

You can enter 1-12 months of detailed usage data. More months = more accurate seasonal analysis.

**For EACH month entered, provide:**

##### 3C-1. Month Selection
- **Input Type**: Dropdown (January-December)
- **Example**: February 2024

##### 3C-2. Electric Usage (kWh) - OPTIONAL per month
- **Input Type**: Number
- **Example**: 350 kWh
- **Where to Find**: Monthly bill under "Elektriciteit verbruik"

##### 3C-3. Electric Cost (€) - REQUIRED per month
- **Input Type**: Euro amount
- **Example**: €105.00
- **Where to Find**: Monthly bill "Elektriciteit totaal"

##### 3C-4. Gas Usage (m³) - OPTIONAL per month
- **Input Type**: Number
- **Example**: 125 m³
- **Where to Find**: Monthly bill under "Aardgas verbruik"

##### 3C-5. Gas Cost (€) - REQUIRED per month
- **Input Type**: Euro amount
- **Example**: €187.50
- **Where to Find**: Monthly bill "Aardgas totaal"

**Benefits of Monthly Data:**
- Calculator can identify seasonal patterns
- Better estimates for insulation vs heating upgrades
- Identifies peak usage months for targeted improvements
- More accurate payback calculations

**Minimum Requirement**: At least 1 month
**Recommended**: At least 3 months including winter and summer
**Optimal**: Full 12 months for complete analysis

---

### 4. Energy Rate Structure - REQUIRED FOR ACCURATE ROI

#### Electric Rate Type - CHOOSE ONE:

##### OPTION A: Constant Rate (Vast Tarief)
**When to Use**: Fixed-price contract with single rate
**Required Field:**
- **Electric Rate (€/kWh)**: Single rate for all hours
- **Example**: €0.30/kWh
- **Where to Find**: Contract or bill "Elektriciteitstarief"

---

##### OPTION B: Variable Rate (Variabel Tarief)
**When to Use**: Market-linked contract with monthly changing rates
**Required Field:**
- **Average Variable Rate (€/kWh)**: Your average rate over past year
- **Example**: €0.28/kWh
- **How to Calculate**: Annual electric cost ÷ annual kWh usage
- **Where to Find**: Annual statement
- **Note**: Rate changes monthly with market

---

##### OPTION C: Dual Rate (Dubbeltarief) - High/Low
**When to Use**: Contract with peak/off-peak pricing
**Required Fields:**

**C-1. High Rate (€/kWh)**
- **When Active**: Peak hours (typically 7am-11pm weekdays)
- **Example**: €0.35/kWh
- **Where to Find**: Contract "Hoog tarief" or "Normaal tarief"

**C-2. Low Rate (€/kWh)**
- **When Active**: Off-peak (nights, weekends)
- **Example**: €0.20/kWh
- **Where to Find**: Contract "Laag tarief" or "Dal tarief"

**C-3. % Usage During High Rate**
- **Input Type**: Percentage (0-100)
- **Typical Values**: 60-70% for most households
- **Example**: 65%
- **How to Estimate**:
  - Most people work 9-5: 60-65%
  - Home all day: 70-75%
  - Night shift worker: 40-50%
- **Where to Find**: Some bills show "Hoog/Laag" breakdown

**Calculator Uses This To**: Calculate weighted average rate for ROI

---

#### Gas Rate Type - CHOOSE ONE:

##### OPTION A: Constant Gas Rate (Vast Tarief)
**When to Use**: Fixed-price gas contract
**Required Field:**
- **Gas Rate (€/m³)**: Single rate per cubic meter
- **Example**: €1.50/m³
- **Where to Find**: Contract or bill "Aardgastarief"

---

##### OPTION B: Variable Gas Rate (Variabel Tarief)
**When to Use**: Market-linked gas contract
**Required Field:**
- **Average Variable Rate (€/m³)**: Your average rate over past year
- **Example**: €1.45/m³
- **How to Calculate**: Annual gas cost ÷ annual m³ usage
- **Where to Find**: Annual statement
- **Note**: Rate changes monthly with market

---

### 5. At Least One Energy Improvement ✳️

**Must select at least ONE improvement with cost:**

#### Available Improvements:
1. **Attic/Roof Insulation** - Upgrade to Rc 6.0+ (€2,500)
2. **Cavity Wall Insulation** - Fill walls or external (€3,500)
3. **Energy-Efficient Windows** - HR++ or triple glazing (€7,000)
4. **High-Efficiency Heating** - Heat pump or HR++ boiler (€10,000)
5. **Solar Panels** - Offset electricity usage (€8,000 + % offset)
6. **Draught Proofing** - Air sealing (€1,200)
7. **Smart Thermostat** - Programmable control (€200)

**For each selected improvement, REQUIRED:**
- Cost in Euros (€)
- For Solar Panels ONLY: Also provide % of electric use to offset (60-100%)

---

## OPTIONAL FIELDS (Improve Accuracy)

### 6. File Upload - Energy Bills (OPTIONAL but HIGHLY RECOMMENDED)

**Upload Options:**
- **Annual Statement** (PDF) - Best option
- **Monthly Bills** (PDF, image, CSV)
- **CSV Export** from energy provider website

**Accepted File Types:**
- PDF (.pdf)
- Images (.jpg, .png)
- CSV/Excel (.csv, .xlsx)
- Text (.txt)

**What Calculator Does:**
- Automatically extracts cost and usage data
- Pre-fills all energy fields
- Identifies your rate structure
- Calculates seasonal patterns

**Benefits:**
- Saves manual data entry time
- More accurate than memory
- Reduces input errors
- Better seasonal analysis

**File Upload is Optional Because:**
- Some users don't have digital bills
- Manual entry still works fine
- Upload is convenience feature only

---

### 7. Home Age (OPTIONAL)
- **Purpose**: Estimates baseline efficiency
- **Input Type**: Number of years
- **Example**: 25 years old
- **Default**: 25 years if not entered
- **Impact on Calculations**:
  - Older homes (40+ years): Higher savings potential
  - New homes (<10 years): Lower savings potential
  - Used for insulation and heating upgrade estimates

---

### 8. Number of Floors (OPTIONAL)
- **Purpose**: Affects heat distribution and insulation needs
- **Input Type**: Dropdown
- **Options**: 1, 1.5, 2, 3+ floors
- **Default**: 2 floors
- **Impact**: Minor (5-8% variance in estimates)

---

### 9. Heating System Age (OPTIONAL)
- **Purpose**: Determines HVAC upgrade potential
- **Input Type**: Number of years
- **Example**: 15 years
- **Default**: 15 years
- **Impact**: Affects heating upgrade ROI
  - 20+ years old: 40% potential savings
  - 10-15 years: 30% savings
  - <10 years: 20-25% savings

---

### 10. Heating System Type (OPTIONAL)
- **Purpose**: Different systems have different upgrade paths
- **Options**:
  - Natural Gas Boiler (most common)
  - Electric Heating
  - Heat Pump
  - Oil Boiler
- **Default**: Natural Gas Boiler
- **Impact**: Affects heating upgrade calculations

---

### 11. Current Insulation Level (OPTIONAL)
- **Purpose**: Determines insulation upgrade potential
- **Options**:
  - Minimal/None
  - Poor (Rc 2.5 or less)
  - Fair (Rc 3.5)
  - Good (Rc 4.5)
  - Excellent (Rc 6.0+)
- **Default**: Fair (Rc 3.5)
- **Impact**: 
  - Poor insulation: 30-40% savings potential
  - Good insulation: 10-15% savings potential

---

### 12. Window Type (OPTIONAL)
- **Purpose**: Determines window upgrade potential
- **Options**:
  - Single Glazing
  - Double Glazing
  - HR++ Double Glazing
  - Triple Glazing
- **Default**: Double Glazing
- **Impact**:
  - Single to triple: 25% savings
  - Double to triple: 8% savings

---

### 13. Address or Postal Code (OPTIONAL)
- **Purpose**: Regional climate adjustment
- **Input Type**: Text (postcode or address)
- **Example**: 1012 AB Amsterdam
- **Default**: Moderate climate (Randstad region)
- **Impact**: 10-15% accuracy improvement for extreme climates
- **When Important**:
  - Northern Netherlands (colder)
  - Southern Netherlands (milder)
  - Coastal areas (wind exposure)

---

### 14. Energy Label Rating (OPTIONAL but VALUABLE)
- **Purpose**: Provides baseline efficiency benchmark for the home
- **Input Type**: Dropdown selection
- **Options**:
  - **A++++ / A+++** - Nearly zero energy (new passive houses)
  - **A++ / A+** - Very energy efficient (new builds 2021+)
  - **A** - Energy efficient (well-insulated, modern systems)
  - **B** - Good efficiency (recent renovation or 2015+ build)
  - **C** - Average efficiency (typical improved home)
  - **D** - Below average (minimal improvements)
  - **E** - Poor efficiency (old systems, basic insulation)
  - **F** - Very poor (original 1970s-1980s systems)
  - **G** - Extremely poor (pre-1970s, no improvements)
  - **Unknown** - Don't know my label
- **Example**: Label C
- **Where to Find**: 
  - Official certificate from energy assessor
  - Check online: www.ep-online.nl (with address)
  - Required for home sales (valid 10 years)
  - Free to look up if assessed previously
- **Default**: Unknown (calculator estimates based on age/systems)
- **Impact on Calculations**:
  - **A++ to A**: Limited improvement potential (5-15% savings)
  - **B to C**: Moderate improvement potential (15-30% savings)
  - **D to E**: High improvement potential (30-50% savings)
  - **F to G**: Very high potential (50-70% savings)
- **How Calculator Uses This**:
  - Overrides generic age-based efficiency assumptions
  - More accurate baseline energy use estimates
  - Better improvement priority recommendations
  - Validates entered energy bills against label
  - Predicts label improvement after upgrades
- **Why It's Valuable**:
  - Official measurement by certified assessor
  - Accounts for all efficiency factors combined
  - More reliable than estimating from age alone
  - Shows impact of improvements on home value
- **Label Impact on Home Value**:
  - A label vs G label: €15,000-€30,000 higher value
  - Each label step up: approximately €3,000-€5,000
  - Not calculated in ROI but real financial benefit
- **After Improvements**:
  - Calculator estimates new label after upgrades
  - Example: Label E → Label B (typical full renovation)
  - Useful for resale planning

---

### 15. Existing Solar Panel System (OPTIONAL - If Installed)

**Skip this section if you don't have solar panels yet**

#### 15A. Number of Solar Panels (PV Cells)
- **Purpose**: Calculates existing solar production to avoid over-sizing new additions
- **Input Type**: Number of panels
- **Example**: 10 panels
- **Typical Ranges**:
  - Small system: 6-8 panels (2-2.5 kWp)
  - Medium system: 10-14 panels (3-4.5 kWp)
  - Large system: 16-24 panels (5-8 kWp)
- **Where to Find**:
  - Installation invoice
  - Count panels on roof
  - Inverter display (shows kWp total)
  - Online monitoring portal
- **Used For**:
  - Current annual production estimate
  - Remaining roof capacity calculation
  - Additional panel ROI (if adding more)
  - Saldering (net metering) optimization

#### 15B. Panel Wattage (Optional)
- **Purpose**: More accurate production calculation
- **Input Type**: Watts per panel (Wp)
- **Example**: 350 Wp
- **Typical Values**:
  - Older panels (pre-2015): 250-280 Wp
  - Standard (2015-2020): 280-330 Wp
  - Modern (2020-2023): 350-400 Wp
  - High-efficiency (2023+): 400-450 Wp
- **Default**: 350 Wp if not specified
- **Where to Find**: Panel datasheet, invoice, or label on panel

#### 15C. Installation Year
- **Purpose**: Estimates panel degradation and remaining system life
- **Input Type**: Year (2000-2025)
- **Example**: 2018
- **Used For**:
  - Production degradation (0.5-1% per year)
  - Warranty remaining calculation
  - Inverter replacement planning (10-15 year life)
  - Considers performance loss over time
- **Impact**:
  - New system (0-2 years): 100% efficiency
  - 5 years old: ~97% efficiency
  - 10 years old: ~93% efficiency
  - 15 years old: ~88% efficiency
  - 25 years old: ~80% efficiency (typical warranty end)

#### 15D. Inverter Type
- **Purpose**: Determines system efficiency and upgrade potential
- **Input Type**: Dropdown selection
- **Options**:
  - **String inverter (basic)** - Single inverter for all panels
  - **String inverter with optimizers** - Per-panel optimization
  - **Micro-inverters** - Individual inverter per panel
  - **Hybrid inverter** - Includes battery capability
  - **Unknown** - Don't know type
- **Example**: String inverter with optimizers
- **Where to Find**: Installation documentation, inverter label
- **Impact on Calculator**:
  - **Basic string**: 95-97% efficiency, shade affects all panels
  - **With optimizers**: 97-99% efficiency, panel-level optimization
  - **Micro-inverters**: 96-98% efficiency, maximum flexibility
  - **Hybrid**: Battery-ready, future expansion option
- **Upgrade Recommendations**:
  - Basic string + shading issues → Consider optimizers
  - Any type → Battery addition capability check

#### 15E. Current Annual Production (Optional but Helpful)
- **Purpose**: Validates system performance vs expected
- **Input Type**: kWh per year
- **Example**: 3,500 kWh/year
- **Where to Find**:
  - Inverter display (yearly total)
  - Online monitoring app (SolarEdge, Enphase, etc.)
  - Smart meter readings
  - Annual energy statement (solar production line)
- **Used For**:
  - Performance verification (underperforming system detection)
  - Accurate offset calculation
  - ROI validation of existing system
  - Comparison to theoretical production
- **Expected Production**:
  - Netherlands average: 900-1,000 kWh per kWp per year
  - 3.5 kWp system: 3,150-3,500 kWh/year
  - South-facing optimal: +10-15%
  - East/West: -15-20%
  - With shading: -20-50%

#### How Existing Solar Data is Used:

**1. Avoids Duplicate Recommendations**
- If you already have 10 panels producing 3,500 kWh
- Calculator won't recommend "add solar panels"
- Instead shows: "Optimize existing system" or "Add battery storage"

**2. Calculates Remaining Potential**
- Roof capacity: Estimates remaining space
- Current offset: Already covering X% of electric use
- Additional potential: Can add Y more panels
- ROI comparison: Existing vs adding more

**3. System Health Check**
- Expected vs actual production comparison
- Flags underperforming systems
- Recommends: Panel cleaning, inverter check, optimizer upgrade

**4. Integration with Other Upgrades**
- Heat pump + existing solar = better ROI
- Battery storage sizing based on current production
- EV charger + solar optimization

---

### 16. Heat Pump System (OPTIONAL - If Installed)

**Skip if you don't have a heat pump**

#### 16A. Heat Pump Type
- **Purpose**: Determines heating/cooling efficiency and upgrade potential
- **Input Type**: Dropdown selection
- **Options**:
  - **Air-to-water (Lucht/water)** - Most common in NL
  - **Ground-source (Bodem/water)** - Highest efficiency
  - **Air-to-air (Lucht/lucht)** - Heating + cooling, no radiators
  - **Hybrid (with gas boiler)** - Switches between heat pump/gas
  - **Unknown/Not sure**
- **Example**: Air-to-water heat pump
- **Where to Find**: Installation documents, outdoor unit label
- **Impact**:
  - Air-to-water: SCOP 3.0-4.5, retrofit-friendly
  - Ground-source: SCOP 4.0-5.5, highest running cost savings
  - Air-to-air: SEER 3.5-5.0, provides cooling also
  - Hybrid: Optimizes based on energy prices

#### 16B. Installation Year
- **Purpose**: Estimates efficiency and remaining warranty
- **Input Type**: Year (2000-2025)
- **Example**: 2020
- **Used For**:
  - Modern efficiency assumptions (newer = better SCOP)
  - Warranty status (typically 5-10 years)
  - Considers technology improvements over time
- **Impact**:
  - Pre-2015: SCOP 2.5-3.5
  - 2015-2020: SCOP 3.5-4.0
  - 2020+: SCOP 4.0-5.0
  - 2023+: SCOP 4.5-5.5 (latest technology)

#### 16C. Capacity (kW) - Optional
- **Purpose**: Validates proper sizing for home volume
- **Input Type**: Number (kW thermal output)
- **Example**: 8 kW
- **Typical Sizing**: 50-80 W per m³ of home volume
- **For 250 m³ home**: 12.5-20 kW needed
- **Where to Find**: Unit specifications, installation docs
- **Used For**:
  - Checks if system is undersized/oversized
  - Validates against home volume
  - Recommends capacity if planning upgrade

#### 16D. Provides Hot Water?
- **Purpose**: Determines if separate water heating is needed
- **Input Type**: Yes/No
- **Options**:
  - **Yes** - Integrated hot water tank
  - **No** - Separate water heating (gas/electric boiler)
- **Impact on Calculator**:
  - If Yes: No water heating upgrade needed
  - If No: May recommend heat pump water heater
  - Affects total energy savings calculation

#### How Heat Pump Data is Used:

**1. Accurate Energy Cost Attribution**
- Separates space heating from other uses
- Validates heat pump efficiency claims
- Compares actual vs expected performance

**2. Upgrade Path Recommendations**
- Existing air-to-water → Consider ground-source for max efficiency
- Old heat pump (<2015) → Upgrade to modern SCOP 4.5+ unit
- Heat pump without hot water → Add heat pump water heater

**3. Integration Optimization**
- Heat pump + solar panels = best synergy
- Heat pump + floor heating = optimal efficiency
- Heat pump + battery = maximize self-consumption

**4. Prevents Redundant Recommendations**
- Won't suggest "install heat pump" if you already have one
- Instead suggests: Optimize settings, add thermal storage, etc.

---

### 17. Air Conditioning System (OPTIONAL - If Installed)

#### 17A. Air Conditioning Type
- **Purpose**: Accounts for cooling energy use, identifies efficiency
- **Input Type**: Dropdown selection
- **Options**:
  - **None** - No air conditioning
  - **Portable units** - Mobile AC units (least efficient)
  - **Split system (1-2 units)** - Wall-mounted indoor units
  - **Multi-split (3+ units)** - Multiple indoor units, 1 outdoor
  - **Ducted central AC** - Whole-home ductwork system
  - **Heat pump (reversible)** - Already counted in heat pump section
- **Example**: Split system (2 units)
- **Where to Find**: Indoor unit count, installation docs

#### 17B. Usage Pattern (Optional)
- **Purpose**: Estimates cooling energy consumption
- **Input Type**: Dropdown
- **Options**:
  - **Rarely (heat waves only)** - <10 days/year
  - **Summer months** - June-August regularly
  - **Extended season** - May-September
  - **Year-round** - For server rooms, home offices, etc.
- **Used For**:
  - Estimates cooling energy cost
  - Identifies high AC usage homes
  - Solar panel sizing includes cooling load

#### How AC Data is Used:

**1. Summer Electric Bill Explanation**
- High summer bills = AC usage identified
- Separates cooling from other electric use
- Better annual cost modeling

**2. Solar Panel Optimization**
- AC use coincides with solar production (sunny = hot)
- Excellent solar + AC synergy
- May justify larger solar system

**3. Efficiency Recommendations**
- Old portable units → Modern split system (3x more efficient)
- Excessive AC use → Better insulation to reduce load

---

### 18. Ventilation System (OPTIONAL)

#### 18A. Ventilation Type
- **Purpose**: Impacts heating energy loss and indoor air quality
- **Input Type**: Dropdown selection
- **Options**:
  - **Natural (windows/vents)** - No mechanical system
  - **Mechanical exhaust (C-system)** - Extract fans only
  - **Balanced (D-system)** - Supply + exhaust, no heat recovery
  - **Balanced with heat recovery (WTW)** - Energy-efficient
  - **Demand-controlled (CO2 sensors)** - Smart ventilation
  - **Unknown** - Not sure what type
- **Example**: Balanced with heat recovery (WTW)
- **Where to Find**: Installation docs, look for WTW unit in attic/basement

#### 18B. Heat Recovery Efficiency (if WTW system)
- **Purpose**: Accurate heat loss calculation
- **Input Type**: Percentage (0-100%)
- **Example**: 85%
- **Typical Values**:
  - Basic WTW: 70-80%
  - Standard: 80-90%
  - High-efficiency: 90-95%
- **Where to Find**: System specifications, WTW unit label
- **Default**: 85% if not specified

#### How Ventilation Data is Used:

**1. Heating Energy Calculation Adjustment**
- Natural ventilation: High heat loss (no recovery)
- WTW system: Reduced heat loss by recovery %
- More accurate heating upgrade savings

**2. Recommendations Based on Type**
- Natural/exhaust only → Recommend WTW system upgrade
- Old WTW (<80% efficiency) → Upgrade to 90%+ modern unit
- No system → Balanced WTW as improvement option

**3. Indoor Air Quality Context**
- Poor ventilation + high heating bills = WTW recommended
- Good WTW system = maintains efficiency + air quality

---

### 19. Floor Heating System (OPTIONAL - If Installed)

#### 19A. Do You Have Floor Heating?
- **Purpose**: Affects heat pump efficiency and comfort
- **Input Type**: Yes/No dropdown
- **Options**: Yes (vloerverwarming) / No

#### 19B. Floor Heating Location (if Yes)
- **Purpose**: Determines heating system coverage and efficiency
- **Input Type**: Multi-select checkboxes
- **Options**:
  - **Living room (woonkamer)**
  - **Kitchen (keuken)**
  - **Bathrooms (badkamers)**
  - **Bedrooms (slaapkamers)**
  - **Hallways (gangen)**
  - **Entire ground floor (hele begane grond)**
  - **Entire house (hele huis)**
- **Example**: Living room + Kitchen + Bathrooms
- **Where to Find**: Installation docs, real estate listing (Funda)

#### 19C. Floor Heating Type (Optional)
- **Purpose**: Determines compatibility with heat pump
- **Input Type**: Dropdown
- **Options**:
  - **Wet system (water-based)** - Most common, heat pump compatible
  - **Electric (resistance cables)** - High running cost
  - **Unknown**
- **Default**: Wet system (water-based)

#### How Floor Heating Data is Used:

**1. Heat Pump Optimization**
- Floor heating present = LOWER temperature needed (35-45°C)
- Radiators only = HIGHER temperature needed (55-70°C)
- Floor heating + heat pump = 30-40% more efficient
- Best COP achieved with floor heating

**2. System Compatibility**
- Floor heating throughout → Heat pump highly recommended
- Partial floor heating → Hybrid or low-temp radiators needed
- No floor heating → Check radiator upgrade for heat pump

**3. Comfort & Efficiency Balance**
- Floor heating areas = optimal heat pump zones
- Non-floor heated areas = may need radiator upgrades
- Calculator identifies best heat pump configuration

**4. Investment Priorities**
- Have floor heating → Heat pump upgrade priority HIGH
- No floor heating → Consider floor heating + heat pump together
- Partial → Extend floor heating or upgrade radiators

---

### 20. Floor Plan Upload (OPTIONAL but VERY VALUABLE)

#### 20A. Upload Floor Plan
- **Purpose**: Enables room-by-room analysis and targeted recommendations
- **Input Type**: File upload (PDF, JPG, PNG)
- **Accepted Files**:
  - Funda listing floor plan (plattegrond)
  - Architect drawings
  - Real estate brochure plans
  - Hand-drawn sketch with dimensions
  - CAD drawings
- **Example**: Funda_Plattegrond.pdf
- **File Size Limit**: 10 MB
- **Where to Find**:
  - Funda listing (download floor plan)
  - Real estate purchase documents
  - Architect/builder records
  - Municipality building permits

#### What Calculator Extracts from Floor Plan:

**1. Room Dimensions & Areas**
- Auto-detects room sizes (if labeled)
- Validates total m² entry
- Calculates room-by-room heating needs

**2. Room Identification**
- Living room, bedrooms, kitchen, bathrooms
- Identifies wet rooms (bathroom/kitchen)
- Locates exterior walls (higher heat loss)

**3. Heating Zone Analysis**
- Compares floor plan to floor heating locations
- Identifies unheated rooms
- Recommends targeted heating upgrades

**4. Window/Wall Analysis**
- Counts windows per room (if shown)
- Estimates exterior wall area
- Calculates insulation potential per room

**5. System Placement Recommendations**
- Optimal heat pump outdoor unit location
- Solar panel roof orientation (if roof shown)
- Ventilation duct routing feasibility
- Water heater placement options

#### How Floor Plan Enhances Calculations:

**Manual Entry (No Floor Plan):**
- Total m² and volume only
- Generic heating distribution assumed
- Average savings estimates

**With Floor Plan:**
- Room-by-room heating analysis
- Targeted insulation recommendations
- Precise HVAC sizing per zone
- Identifies problem areas (cold north-facing rooms)

**Example Insights:**
- "Master bedroom on north wall: Prioritize wall insulation"
- "Large south-facing living room: Excellent for floor heating + heat pump"
- "Small bathrooms: Consider separate electric heating supplement"

#### Floor Plan Analysis Output:

**Visual Room Map with:**
- Color-coded heat loss (red = high loss, green = efficient)
- Recommended improvements per room
- Equipment placement suggestions
- Before/after energy use comparison

**Priority Recommendations:**
1. Living room (40% of heating): Floor heating + heat pump
2. North bedrooms (25% heat loss): Wall insulation priority
3. Bathroom (hot water intensive): Heat pump water heater
4. South roof (solar potential): 12 panels optimal

---

### How All System Data Works Together:

**Example: Complete System Analysis**

**Home Profile:**
- Volume: 300 m³
- Energy Label: D
- Solar: 10 panels (350W, 2019, string inverter)
- Heat pump: Air-to-water (2020, 8 kW)
- Ventilation: WTW (85% recovery)
- Floor heating: Living room + kitchen only
- AC: 2 split units (summer use)
- Water: 120 m³/year
- Floor plan: Uploaded from Funda

**Calculator Comprehensive Analysis:**

**Current Performance:**
- Solar offset: 35% of electric use (3,500 kWh/year)
- Heat pump: Good efficiency but limited by radiators in bedrooms
- WTW: Recovering 85% of ventilation heat loss ✓
- Floor heating zones: Optimal but only 45% of home
- Hot water: Provided by heat pump ✓
- AC summer load: 800 kWh/year (peak solar production) ✓

**Room-by-Room Findings (from floor plan):**
- Living room: Floor heating + heat pump = very efficient ✓
- Kitchen: Floor heating = good ✓
- Master bedroom (north): Radiators + poor insulation = high heat loss ⚠️
- Kids bedrooms: Radiators = moderate efficiency
- Bathrooms: No floor heating = discomfort issue

**Prioritized Recommendations:**

1. **Extend floor heating to bedrooms** (€4,500)
   - Enables full heat pump efficiency
   - Saves €320/year on heating
   - Improves comfort significantly
   - Payback: 14 years

2. **Add solar panels (6 more)** (€2,400)
   - Increase to 90% electric offset
   - Remaining roof space on south side (from floor plan)
   - Covers AC summer use completely
   - Saves €280/year
   - Payback: 8.5 years

3. **Wall insulation (north bedrooms only)** (€2,200)
   - Targeted based on floor plan analysis
   - Reduces bedroom heating load 40%
   - Saves €180/year
   - Payback: 12 years

4. **Add optimizers to existing solar** (€1,200)
   - Improve performance 5-8%
   - Helps with morning/evening shading (if present)
   - Saves €105/year
   - Payback: 11.5 years

**Total Investment**: €10,300
**Total Annual Savings**: €885/year
**Combined Payback**: 11.6 years
**New Energy Label**: C (from D)
**Home Value Increase**: ~€8,000

**Without floor plan**: Generic recommendations, less precise savings
**With all system data**: Targeted, optimized improvement sequence

---

### Summary of New System Fields:

| Field | Required? | Impact | Best Practice |
|-------|-----------|--------|---------------|
| **Solar panels (#)** | No | High if installed | Always enter if you have solar |
| **Panel installation year** | No | Medium | Include for degradation calc |
| **Inverter type** | No | Medium | Helps identify upgrade path |
| **Heat pump type** | No | High if installed | Critical for accurate savings |
| **Heat pump year** | No | Medium | Shows if upgrade worthwhile |
| **AC system** | No | Low-Medium | Explains summer electric bills |
| **Ventilation type** | No | Medium | Affects heating calculations |
| **Floor heating** | No | High | Major impact on heat pump ROI |
| **Floor heating zones** | No | High | Enables targeted recommendations |
| **Floor plan upload** | No | Very High | Best ROI improvement: room analysis |

**Recommendation Priority:**
1. 🌟 Floor plan (if available from Funda) - Biggest accuracy boost
2. ⭐ Floor heating details (if installed) - Critical for heat pump decisions
3. ⭐ Existing solar system (if installed) - Avoid duplicate recommendations
4. ⭐ Heat pump details (if installed) - Validates performance
5. Ventilation type - Good for heating calculations
6. AC system - Explains summer usage patterns

---

### 15. Water Usage (OPTIONAL - Heating Insight)
- **Purpose**: Estimates hot water heating energy consumption
- **Input Type**: Choose ONE method:

#### METHOD A: Monthly Water Bill (€)
- **Input Type**: Euro amount
- **Example**: €45/month
- **Typical Range**: €30-€80/month for Dutch households
- **Where to Find**: Water company bill (Waternet, Vitens, etc.)
- **What's Included**: 
  - Drinking water (drinkwater)
  - Wastewater (afvalwater/rioolheffing)
  - Environmental charges
- **Default**: Not entered

#### METHOD B: Water Usage (m³/month or m³/year)
- **Input Type**: Cubic meters per month OR per year
- **Example**: 
  - 8 m³/month (96 m³/year)
  - 120 m³/year
- **Typical Ranges**:
  - Single person: 35-50 m³/year (3-4 m³/month)
  - Couple: 60-80 m³/year (5-7 m³/month)
  - Family (3-4): 100-140 m³/year (8-12 m³/month)
  - Large family (5+): 150-200 m³/year (12-17 m³/month)
- **Where to Find**: 
  - Water bill "Verbruik" section
  - Meter reading: current - last year
  - Online account at water company
- **Default**: Not entered

#### METHOD C: Number of People in Household
- **Input Type**: Number (1-10+)
- **Example**: 3 people
- **Calculator Estimates**: ~35 m³/year per person
- **Used When**: No water bill data available
- **Accuracy**: Rough estimate only
- **Default**: Not entered

---

### How Water Usage Data is Used:

#### 1. Hot Water Energy Calculation
- **Assumption**: ~80% of home water use requires heating
  - Showers: 60-70% of hot water use
  - Kitchen/dishes: 15-20%
  - Laundry: 10-15%
  - Other: 5-10%
- **Energy Required**: 
  - Heat 1 m³ water from 10°C to 60°C: ~58 kWh
  - Annual calculation: (m³/year × 0.8) × 58 kWh
  - Example: 100 m³/year → 4,640 kWh for hot water
- **Cost Calculation**:
  - Gas heating: kWh ÷ boiler efficiency × gas rate
  - Electric heating: kWh × electric rate
  - Heat pump: kWh ÷ COP × electric rate

#### 2. Improvement Impact on Hot Water
Different improvements affect hot water costs differently:

**Heat Pump Water Heater** (Warmtepompboiler):
- Saves 50-70% on water heating energy
- ROI calculation shows separate payback
- Typical cost: €1,500-€2,500

**Solar Water Heater** (Zonneboiler):
- Saves 40-60% on water heating (summer more)
- Works with gas or electric systems
- Typical cost: €2,500-€4,000
- May qualify for ISDE subsidy

**Shower Heat Recovery** (Douchewtw):
- Recovers 40-50% of shower heat
- Low cost improvement
- Typical cost: €500-€1,000

**Insulated Hot Water Tank**:
- Reduces standby losses 30-50%
- Very low cost
- DIY: €50-€150

**High-Efficiency Boiler**:
- Better hot water efficiency
- Combined with space heating upgrade

#### 3. Usage Pattern Insights

**High Water Use (>150 m³/year for 3-4 people)**:
- Indicates potential for water-saving improvements
- Possible leaks or inefficient fixtures
- High hot water heating cost
- Priority: Water heating efficiency upgrades

**Low Water Use (<80 m³/year for 3-4 people)**:
- Already efficient water usage
- Lower hot water heating cost
- Less benefit from water heating upgrades

**Compared to Gas Bill**:
- If water use HIGH but gas bill LOW → Possible electric water heating
- If water use LOW but gas bill HIGH → Space heating is main cost
- If both HIGH → Both space and water heating need attention

#### 4. Hot Water Heating System Detection

**If Water Usage + Gas Bill Provided**:
Calculator can estimate:
- % of gas bill for hot water vs space heating
- Typical split: 15-25% hot water, 75-85% space heating
- Higher water use = higher % for hot water
- Helps prioritize: space heating vs water heating upgrades

**If Water Usage + Electric Bill Provided**:
- May indicate electric water heater (boiler)
- Can estimate electric water heating cost
- Shows opportunity for heat pump water heater

#### 5. Seasonal Analysis (if monthly water data)

**Monthly Water Usage Pattern**:
- Summer: Lower water use typical (no heating needed)
- Winter: Similar water use but more hot water showers
- Identifies shower/bath preferences

**Combined with Energy Bills**:
- Summer gas bill spike + constant water = hot water only
- Helps separate space heating from water heating costs
- More accurate improvement recommendations

---

### Water Usage: Why It's Optional but Useful

**Required?** No - calculator works without it

**Benefits if Provided**:
1. ✅ Identifies 15-25% of energy bill (hot water portion)
2. ✅ Recommends water heating specific upgrades
3. ✅ More accurate heat pump sizing (includes hot water load)
4. ✅ Shows if water-saving measures would help
5. ✅ Detects electric water heating (high cost)
6. ✅ Improves gas vs electric cost split accuracy

**When to Definitely Include**:
- Considering heat pump (needs hot water capacity sizing)
- High energy bills with unknown cause
- Evaluating solar water heater
- Planning comprehensive renovation
- Home has electric water heater

**When You Can Skip**:
- Quick estimate only
- Only interested in insulation/solar panels
- Very low water usage household
- Focus on space heating only

---

### Water Usage Examples:

**Example 1: Family with High Bills**
- People: 4
- Water: 180 m³/year (15 m³/month)
- Hot water energy: ~8,350 kWh/year
- At €1.50/m³ gas: ~€187/year for hot water
- **Insight**: Hot water is 18% of €1,200 gas bill
- **Recommendation**: Consider heat pump water heater

**Example 2: Couple with Electric Heating**
- People: 2
- Water: 65 m³/year
- Hot water energy: ~3,000 kWh/year
- At €0.30/kWh electric: €900/year for hot water!
- **Insight**: Hot water is major cost (electric heating)
- **Recommendation**: Priority upgrade to heat pump water heater (saves €600/year)

**Example 3: Efficient Single Person**
- People: 1
- Water: 40 m³/year
- Hot water energy: ~1,850 kWh/year
- At €1.50/m³ gas: ~€42/year
- **Insight**: Hot water minimal cost
- **Recommendation**: Skip water heating upgrades, focus on space heating

---

### Water Data Entry Options:

**Option 1: Upload Water Bill PDF**
- Auto-extracts m³ usage and cost
- Identifies billing period (monthly/annual)
- Fastest method

**Option 2: Enter Usage Manually**
- Monthly m³ or annual m³
- Calculator handles conversion

**Option 3: Enter Bill Amount**
- Less accurate but acceptable
- Calculator estimates m³ based on €/m³ average

**Option 4: Enter Household Size**
- Least accurate
- Quick estimate only
- Uses 35 m³/person/year assumption

---

### Water Rate Information (for reference):

**Typical Netherlands Water Costs (2025)**:
- Drinking water: €1.20-€1.80/m³
- Wastewater: €1.50-€2.50/m³  
- **Total**: €2.70-€4.30/m³ combined
- **Average**: €3.50/m³ total

**Not Used for ROI Calculation** (water cost savings are minimal)
**Used Only For**: Hot water energy estimation

---

## SUMMARY: MINIMUM REQUIRED INPUT

To calculate ROI, you MUST provide:

### Absolute Minimum (Quick Calculation):
1. ✅ Square Meters (m²)
2. ✅ Total Volume (m³) - or will auto-calculate
3. ✅ Energy Data - ONE of:
   - Simple: Monthly electric (€) + gas (€) bills
   - Annual: Total annual electric (€) + gas (€) costs
   - Detailed: At least 1 month with costs
4. ✅ Rate Structure - ONE of:
   - Electric: Constant, Variable, or Dual rate
   - Gas: Constant or Variable rate
5. ✅ At least one improvement selected with cost (€)

### Recommended for Accuracy:
- Upload annual energy statement (PDF)
- Use "Detailed Monthly Data" method if available
- Specify exact rate structure (dual rate if applicable)
- Provide home age and current system details
- **Include energy label if known** (official certificate)
- **Add water usage data** if considering water heating upgrades

---

## OPTIONAL FIELDS PRIORITY RANKING

### High Impact (Strongly Recommended):
1. **Energy Label Rating** - Single most accurate efficiency indicator
2. **File Upload** - Saves time and increases accuracy
3. **Exact Rate Structure** - Critical for dual-rate contracts
4. **Water Usage** - Important if high energy bills or considering heat pump

### Medium Impact (Helpful):
5. Home Age - Good efficiency estimate
6. Current Insulation Level - Affects upgrade potential
7. Heating System Age & Type - For HVAC upgrades

### Low Impact (Nice to Have):
8. Window Type - Minor refinement
9. Number of Floors - Small adjustment
10. Postal Code - Only for extreme climates

---

## DATA ENTRY METHODS COMPARISON

| Method | Required Fields | Time to Complete | Accuracy | Best For |
|--------|----------------|------------------|----------|----------|
| **Simple** | 2 monthly bills + rates | 2 minutes | ±15% | Quick estimate |
| **Annual** | 2 annual totals + rates | 3 minutes | ±10% | Better accuracy |
| **Detailed** | Monthly breakdowns | 10-15 minutes | ±5% | Maximum accuracy |
| **File Upload** | Upload PDF | 1 minute | ±5% | Easiest + most accurate |

---

## FIELD DEPENDENCIES

### If you select "Dual Rate" for electricity:
- THEN you must provide: High rate, Low rate, % high usage

### If you select "Detailed Monthly Data":
- THEN you must provide: At least 1 month with costs
- OPTIONAL: Usage data (kWh, m³) for that month

### If you select "Solar Panels":
- THEN you must provide: Cost AND % of electric use to offset

### If you upload a file:
- THEN Simple/Annual fields auto-populate
- BUT you can still manually override any value

---

## VALIDATION RULES

### Numeric Fields:
- Must be positive numbers
- Square meters: 20-500 m² (reasonable range)
- Volume: 50-1500 m³ (reasonable range)
- Monthly bills: €1-€1000 (catches typos)
- Rates: €0.01-€2.00 per unit (reasonable range)
- Percentages: 0-100%

### Required Field Logic:
```
IF entry_method = "Simple"
  THEN require: electricBill, gasBill
  
IF entry_method = "Annual"
  THEN require: annualElectric, annualGas
  
IF entry_method = "Detailed"
  THEN require: At least 1 month with electricCost AND gasCost
  
IF elec_rate_type = "Dual"
  THEN require: electricRateHigh, electricRateLow, highRatePct
ELSE IF elec_rate_type = "Variable"
  THEN require: electricRateVar
ELSE
  THEN require: electricRate
  
IF gas_rate_type = "Variable"
  THEN require: gasRateVar
ELSE
  THEN require: gasRate
  
IF solar_panels_selected = TRUE
  THEN require: cost AND offsetPct
```

---

## FILE UPLOAD SPECIFICATIONS

### Supported File Types:
- **PDF**: Annual statements, monthly bills
- **Images**: JPG, PNG of paper bills
- **CSV**: Export from energy provider
- **Excel**: XLSX files with usage data

### What Data is Extracted:
1. **From Annual Statements**:
   - Total electric cost (€)
   - Total gas cost (€)
   - Total electric usage (kWh) - if shown
   - Total gas usage (m³) - if shown
   - Rate structure (fixed/variable)

2. **From Monthly Bills**:
   - Month
   - Electric cost (€)
   - Electric usage (kWh)
   - Gas cost (€)
   - Gas usage (m³)
   - Rates (€/kWh, €/m³)

3. **From CSV Files**:
   - Expects columns: Date, Electric_kWh, Electric_Cost, Gas_m3, Gas_Cost
   - Auto-detects column headers
   - Handles Dutch and English headers

### File Size Limits:
- Maximum: 10 MB per file
- PDFs: Up to 50 pages
- Images: Up to 4000x4000 pixels

### Privacy Note:
- Files processed locally in browser
- No data sent to servers
- Files not stored or saved

---

## EXAMPLES BY USER TYPE

### Example 1: Quick User (Minimum Input)
**Goal**: Fast estimate
**Time**: 3 minutes

**Required Input:**
- Square meters: 100 m²
- Volume: 250 m³
- Monthly electric bill: €120
- Monthly gas bill: €150
- Electric rate: €0.30/kWh (constant)
- Gas rate: €1.50/m³ (constant)
- Selected: Solar panels (€8,000, 80% offset)

**Result**: Basic ROI calculation with ±15% accuracy

---

### Example 2: Accurate User (Recommended Input)
**Goal**: Reliable planning
**Time**: 7 minutes

**Required Input:**
- Upload annual statement PDF (auto-fills all costs)
- **Upload floor plan from Funda** (auto-analyzes rooms)
- Manual confirm: Dual rate (€0.35 high, €0.20 low, 65% high usage)
- Volume: 260 m³
- Home age: 28 years
- **Energy Label: D** (provides accurate baseline)
- Current insulation: Poor
- **Water usage: 120 m³/year** (or 3 people in household)
- **Existing solar: 8 panels, 300W each, installed 2018, string inverter**
- **Floor heating: Living room + Kitchen**
- Selected: Wall insulation + Heat pump + Add 6 more solar panels

**Result**: Accurate ROI with ±5% accuracy, seasonal analysis, hot water heating insights, label improvement prediction (D→B), room-by-room recommendations, solar expansion analysis

---

### Example 3: Detailed User (Maximum Accuracy)
**Goal**: Investment decision
**Time**: 20 minutes

**Required Input:**
- All monthly data for 12 months (energy + water if available)
- Exact dual rate structure
- **Floor plan upload with room labels**
- **Energy Label: E** (official certificate)
- All optional home system details
- **Existing systems:**
  - Solar: 10×350W panels, 2019, optimizers, producing 3,400 kWh/year
  - Heat pump: Air-to-water, 2020, 8kW, provides hot water
  - Ventilation: WTW system with 85% heat recovery
  - Floor heating: Entire ground floor (60m²)
  - AC: 2 split units, summer use only
- **Water usage: Monthly breakdown** showing seasonal patterns
- Multiple improvements with exact quotes
- Postal code for regional adjustment

**Result**: Highly accurate ROI, monthly breakdown, optimal improvement sequence, hot water vs space heating cost split, predicted label improvement to B or A, room-specific recommendations, system integration analysis, equipment placement suggestions

---

## WHAT HAPPENS AFTER DATA ENTRY

### Calculator Automatically Computes:

1. **Annual Energy Costs**:
   - From simple monthly average, OR
   - From annual totals, OR
   - From monthly data aggregation

2. **Effective Energy Rates**:
   - Weighted average if dual rate
   - Current rate if variable
   - Fixed rate if constant

3. **Usage Patterns** (if monthly data provided):
   - Seasonal variation
   - Peak usage months
   - Heating vs cooling loads
   - Water heating patterns (if water data provided)

4. **Hot Water Analysis** (if water usage provided):
   - Annual hot water heating energy (kWh)
   - Hot water heating cost (€)
   - % of total energy bill for hot water
   - Gas vs electric water heating detection
   - Water heating upgrade ROI

5. **Energy Label Predictions** (if current label provided):
   - Current label verification
   - Predicted label after each improvement
   - Predicted label after all improvements
   - Impact on home value

6. **Improvement Savings**:
   - Per improvement selected
   - Combined total savings
   - Accounts for overlapping benefits
   - Separates space heating vs water heating savings

7. **Financial Metrics**:
   - Total investment cost
   - Annual savings (€)
   - Payback period (years)
   - 20-year net savings
   - ROI percentage
   - Estimated home value increase (from label improvement)

8. **Energy Metrics**:
   - kWh reduction
   - m³ gas reduction
   - % cost reduction
   - CO₂ reduction (kg/year)
   - Energy label improvement

---

## TIPS FOR BEST RESULTS

### For Most Accurate ROI:
1. ✅ Upload your annual energy statement
2. ✅ Specify exact rate type (especially if dual rate)
3. ✅ Provide actual volume measurement
4. ✅ Enter home age and current system details
5. ✅ Use actual improvement quotes, not estimates

### Common Mistakes to Avoid:
❌ Using winter-only gas bill instead of annual average
❌ Forgetting to specify dual rate when applicable
❌ Entering square feet instead of square meters
❌ Not accounting for subsidies in improvement costs
❌ Using retail rates instead of total bill ÷ usage

### Time-Saving Tips:
- Have your annual statement ready before starting
- Use PDF upload instead of manual entry
- Let auto-calculate handle volume (m² × 2.5)
- Start with simple entry, add details later if needed

---

## FIELD REQUIREMENTS BY CALCULATION ACCURACY

| Accuracy Level | Required Fields | Optional Fields | Time |
|---------------|-----------------|-----------------|------|
| **Basic (±15%)** | m², volume, monthly bills, basic rates | None | 3 min |
| **Good (±10%)** | m², volume, annual totals, rate type | Home age, energy label | 5 min |
| **High (±5%)** | All above + monthly data | All home systems, water usage, floor heating | 15 min |
| **Maximum (±3%)** | All above + file uploads | Energy label, floor plan, all installed systems | 10 min |

---

## NEW FEATURES SUMMARY (Version 5.0)

### Energy Label Rating (Field #14)
- **What**: Official A++++ to G rating
- **Impact**: Single most accurate efficiency indicator
- **Value**: Predicts home value increase from improvements

### Water Usage (Field #15)
- **What**: m³/year, m³/month, or € water bill  
- **Impact**: Identifies 15-25% of energy bill (hot water)
- **Value**: Enables water heating upgrade recommendations

### Existing Solar Panel System (Fields #15A-E)
- **What**: Number of panels, wattage, year, inverter type, production
- **Impact**: Prevents duplicate recommendations, shows expansion potential
- **Value**: Validates system performance, identifies upgrade opportunities

### Heat Pump System (Fields #16A-D)
- **What**: Type, year, capacity, hot water capability
- **Impact**: Critical for accurate heating cost modeling
- **Value**: Optimizes heat pump + floor heating + solar integration

### Air Conditioning (Fields #17A-B)
- **What**: Type, usage pattern
- **Impact**: Explains summer electric usage spikes
- **Value**: Shows solar + AC synergy opportunity

### Ventilation System (Fields #18A-B)
- **What**: Type (WTW/balanced/exhaust), heat recovery %
- **Impact**: Adjusts heating loss calculations
- **Value**: Identifies ventilation upgrade potential

### Floor Heating (Fields #19A-C)
- **What**: Yes/No, room locations, system type
- **Impact**: Major factor in heat pump efficiency (30-40% better)
- **Value**: Guides heat pump sizing and ROI calculations

### Floor Plan Upload (Field #20)
- **What**: PDF/image from Funda or architect
- **Impact**: Enables room-by-room analysis and targeted recommendations
- **Value**: Highest accuracy boost - identifies problem areas, optimizes equipment placement

---

## COMPLETE OPTIONAL FIELDS SUMMARY (20 Total)

**Very High Impact (Must have if applicable):**
1. Floor Plan Upload 🌟
2. Energy Label Rating ⭐
3. Existing Solar System ⭐
4. Floor Heating Details ⭐
5. Heat Pump System Info ⭐

**High Impact:**
6. Energy Bill File Upload
7. Exact Rate Structure (dual/variable)
8. Water Usage Data
9. Ventilation System Type

**Medium Impact:**
10. Home Age
11. Current Insulation Level
12. Heating System Age/Type
13. AC System Details

**Low Impact:**
14-20. Window type, floors, postal code, solar details, etc.

---

## SYSTEM INTEGRATION ANALYSIS

When you provide **all installed system data**, calculator performs:

### Cross-System Efficiency Check:
✅ Solar production vs electric usage
✅ Heat pump COP vs floor heating coverage
✅ WTW recovery vs heating requirements
✅ AC load vs solar summer production
✅ Hot water demand vs heating system capacity

### Identifies Synergies:
- Heat pump + floor heating = 35% more efficient
- Solar + AC = perfect timing match (sunny = cooling needed)
- WTW + heat pump = minimal ventilation heat loss
- Solar + heat pump = renewable heating
- Floor plan + all systems = room-level optimization

### Prevents Conflicts:
- Don't recommend solar if roof is full
- Don't suggest heat pump if no floor heating and small radiators
- Don't propose more insulation if Label A already
- Avoid redundant upgrades

### Example Complete Analysis:
**Input**: Floor plan + Label D + 8 solar panels + heat pump + floor heating (partial) + WTW
**Output**: 
- Extend floor heating to bedrooms (unlock full heat pump potential)
- Add 4 solar panels on remaining south roof (from floor plan)
- Upgrade Label D → B
- Total savings: €1,100/year
- Payback: 9.5 years
- Home value: +€12,000

---

**Document Version**: 5.0 Complete System Integration
**Last Updated**: February 2025
**New Fields Added**: 
- Solar panel system (5 sub-fields)
- Heat pump details (4 sub-fields)
- Air conditioning (2 sub-fields)
- Ventilation system (2 sub-fields)
- Floor heating (3 sub-fields)
- Floor plan upload (1 field)
**Total Optional Fields**: 20
**Focus**: English Language Requirements
**Target**: Netherlands residential properties
**Special Feature**: Room-by-room analysis with floor plan
**Currency**: Euro (€)
**Measurements**: Metric (m², m³, kWh, m³, kWp)

---

## PART 3: POST-CALCULATION WORKFLOW

### After Data Entry: What Happens Next

Once you complete entering data and click "Calculate ROI & Savings", the system moves through several phases:

---

### PHASE 1: Instant Analysis & Initial Plan Generation (2-3 seconds)

The calculator performs comprehensive analysis and generates a detailed initial plan.

#### Plan Components:

**A. Current Situation Dashboard**
- Energy Label: Your current rating
- Annual Energy Costs: €X,XXX (breakdown by electric/gas/hot water)
- Energy Intensity: X kWh/m²/year
- Comparison: "X% above/below similar homes"

**B. Existing Systems Performance**
- Solar: X kWp producing X kWh/year (X% self-use)
- Heat Pump: Performance grade (A-F)
- Floor Heating: X% coverage
- Ventilation: X% heat recovery
- Overall System Grade: A-F

**C. Prioritized Recommendations**
Each improvement shows:
1. Investment: €X,XXX (after subsidies)
2. Annual Savings: €XXX/year
3. Payback: X.X years
4. Priority: Critical/High/Medium/Low
5. Label Impact: D→B
6. Why This First: Dependency/ROI explanation

**D. Implementation Timeline**
- Phase 1 (0-3 months): Quick wins
- Phase 2 (3-12 months): Medium investments
- Phase 3 (1-2 years): Major projects
- Phase 4 (2-5 years): Optional upgrades

**E. Financial Summary**
- Total Investment: €XX,XXX
- Available Subsidies: €X,XXX
- Net Cost: €XX,XXX
- Annual Savings: €X,XXX/year
- 20-Year Net Benefit: €XX,XXX
- Home Value Increase: +€X,XXX

**F. Environmental Impact**
- CO₂ Reduction: X,XXX kg/year
- Energy Reduction: XX%

---

### PHASE 2: Plan Review & Customization

Users can interact with the plan:

**Options:**
- Toggle improvements on/off
- Adjust costs (use actual quotes)
- Compare scenarios (minimal/recommended/comprehensive)
- View room-by-room details (if floor plan uploaded)
- Export as PDF, Excel, or share link

**Scenario Comparison Example:**
```
Budget Option    | Recommended    | Comprehensive
€5,000          | €15,000        | €35,000
€450/year saved | €1,150/year    | €1,850/year
Label E→D       | Label E→B      | Label E→A
11.1 yr payback | 13.0 yr        | 18.9 yr
```

---

### PHASE 3: Export & Share Options

**Available Formats:**
1. **PDF Report** - Professional, contractor-ready
2. **Excel Spreadsheet** - Editable calculations
3. **Web Share Link** - Online view (30 days valid)

---

### PHASE 4: 📱 Connect with WhatsApp Energy Advisor (REQUIRED PHONE NUMBER)

#### The Transition from Calculator to Service

After reviewing the initial plan, users see a prominent call-to-action:

```
┌──────────────────────────────────────────────────┐
│  📱 Get Personalized Guidance via WhatsApp       │
│                                                  │
│  Your plan is ready! Connect with our AI        │
│  Energy Advisor for:                            │
│  ✓ Expert refinement of recommendations         │
│  ✓ Vetted contractor matching                   │
│  ✓ Subsidy application assistance               │
│  ✓ Implementation timeline coordination         │
│                                                  │
│  Enter your WhatsApp number:                    │
│  [+31] [__ __________]                          │
│                                                  │
│  ☐ I agree to receive energy advice via         │
│     WhatsApp (Privacy Policy | Unsubscribe)     │
│                                                  │
│  [Start WhatsApp Conversation] →                │
│                                                  │
│  💬 100% Free | 24/7 | English & Nederlands     │
└──────────────────────────────────────────────────┘
```

#### REQUIRED FIELD: Phone Number for WhatsApp

**Field Specification:**
- **Input Type**: Phone number (international format)
- **Format**: +31 6 XXXXXXXX (Netherlands mobile)
- **Validation**:
  - Must be valid NL mobile number
  - Must have WhatsApp installed (auto-checked)
  - Duplicate prevention (one account per number)
- **Privacy**:
  - GDPR compliant
  - Used ONLY for WhatsApp bot communication
  - Not shared with third parties
  - Can delete/unsubscribe anytime
- **Consent**: Required checkbox before submission

**Why WhatsApp?**
- ✅ 99% adoption in Netherlands
- ✅ Already on user's phone (no app install)
- ✅ Conversational interface (easy Q&A)
- ✅ Push notifications (reminders)
- ✅ Multimedia support (photos, docs)
- ✅ Secure & encrypted
- ✅ Preferred for business communication in NL

---

### PHASE 5: WhatsApp Bot Conversation Flow

#### Bot Welcome & Plan Transfer

**First Message (within 30 seconds):**
```
👋 Hi! I'm your Energy Advisor from the ROI Calculator.

I've received your home energy plan:
• 🏠 120m², Label D
• 💡 €3,240/year current costs
• 🎯 €1,150/year savings potential

Top 3 recommendations:
1. Floor heating extension (€4,500)
2. Solar expansion (€2,400)  
3. Wall insulation (€2,200)

How can I help you get started? 🤔

[Quick Reply Options:]
• Explain recommendations
• Find contractors
• Help with subsidies
• Adjust the plan
• Timeline planning
```

#### What the Bot Can Do:

**1. Answer Questions**
```
User: "Why floor heating before insulation?"

Bot: "Great question! 🤔

Your heat pump is limited by bedroom radiators 
needing 55°C water. With floor heating:
• Heat pump runs at 35°C = 35% more efficient
• Unlocks full savings potential
• Annual savings: €320 vs €180

Floor heating first maximizes every future upgrade

[See calculations] [Next question]"
```

**2. Find & Vet Contractors**
```
User: "Need contractor for insulation"

Bot: "I can help! 🔨

For cavity wall insulation in [Your Region]:

⭐ InsulatieBedrijf NL (4.8/5, 230 reviews)
• RVO certified (subsidy qualified)
• Quote range: €2,100-€2,400
[Request Quote]

⭐ WarmteWoning (4.6/5, 187 reviews)
• Full-service energy renovations
• Quote range: €2,300-€2,600
[Request Quote]

I'll send your specs. Quotes in 2-3 days.

[Both] [Choose one]"
```

**3. Navigate Subsidies**
```
User: "How do I get heat pump subsidy?"

Bot: "Let me guide you through ISDE! 💰

Your heat pump qualifies for €2,500-€4,000.

Step-by-step process:
1️⃣ Pre-check eligibility (let's do now)
2️⃣ Get quote (RVO-registered installer)
3️⃣ Submit application (I'll help draft)
4️⃣ Wait approval (4-6 weeks)
5️⃣ Complete installation
6️⃣ Submit proof → Receive payment

Current status: Budget available ✅
Deadline: Year-round rolling

Ready to start pre-check?
[Yes, let's go] [More info first]"
```

**4. Schedule & Coordinate**
```
User: "When should I install what?"

Bot: "Let me create your timeline! 📅

🌸 MARCH-APRIL (Spring):
✅ Apply ISDE heat pump subsidy
✅ Get quotes (insulation + floor heating)
✅ Install smart thermostat (1 day, DIY)

☀️ MAY-JUNE (Summer):
✅ Wall insulation (3-4 days)
✅ Solar expansion (1 day)
✅ Start floor heating (2 weeks)

🍂 AUG-SEPT (Late Summer):
✅ Complete floor heating
✅ Heat pump install (2-3 days)

❄️ OCTOBER (Before heating season):
✅ Testing & optimization

Total: 6-7 months
⚠️ Critical: Start subsidy March!

[Add to calendar] [Adjust timeline]"
```

**5. Track Progress**
```
[After first improvement]

Bot: "🎉 Congratulations!

Smart thermostat installed! ✅

📊 Impact:
• Saves: €145/year
• Payback: 1.4 years
• CO₂ cut: 125 kg/year

💰 Running total:
• Invested: €200
• Saves: €145/year
• Remaining: €9,100 (€1,005/year more)

You're 14% to Label C! 🌟

Next: Wall insulation quotes
[View contractors] [Skip to next]"
```

**6. Troubleshoot**
```
User: "Contractor quote way too high"

Bot: "Let me help analyze 🔍

Estimate: €2,200
Quote: €3,800

Possible reasons:
❓ Different scope?
❓ Premium materials?
❓ Additional repairs?

Actions:
1️⃣ Request detailed breakdown
2️⃣ Get 2 more quotes
3️⃣ Send me quote for review

Can you photo the quote?
I'll analyze within 2 hours.

[Send photo] [Get more quotes]"
```

**7. Proactive Check-ins**
```
[Bot detects 3 weeks no action]

Bot: "👋 Hi! Just checking in.

Haven't moved on wall insulation yet.
Common reasons:

😟 Too busy?
💰 Budget concerns?
🤔 Comparing options?
⚡ Waiting for timing?

No pressure! Here when ready.

Quick wins you COULD do (<1 week):
• Draft excluders (€40, saves €65/yr)
• Pipe insulation (€80, saves €45/yr)

Want these small steps instead? 🎯
[Yes] [Remind me later]"
```

**8. Post-Completion Celebration**
```
[After all improvements done]

Bot: "🎊 CONGRATULATIONS! Complete! ✅

📊 FINAL RESULTS:
━━━━━━━━━━━━━━━━━━━━
💰 Total: €9,300
💵 Saves: €1,150/year
⏱️ Payback: 8.1 years
🏷️ Label: D → B ⬆️⬆️
🌍 CO₂: -3,200 kg/year
🏡 Value: +€12,000

20-YEAR PROFIT: €14,700 📈

Top 15% most efficient homes in NL! 🌟

What's next:
📅 Year 1 checkup (in 12 months)
📊 Optimization tips (seasonal)
💡 Tech updates (as available)

Referral bonus? Share plan:
[Generate link] (They get 10% off, you get €50)

Stay in touch?
[Keep active] [Pause notifications]"
```

#### Bot Intelligence Features:

**Context Awareness:**
- Remembers entire plan
- Tracks conversation history
- Knows all home specifics
- Learns preferences

**Personalization:**
- References YOUR data
- Calculates for YOUR situation
- Adapts language level
- Multi-language (EN/NL auto-detect)

**Visual Communication:**
- Sends annotated floor plans
- Heat loss maps
- Charts and graphs
- Document previews

**Proactive Engagement:**
- Subsidy deadline reminders
- Weather-based install timing
- Seasonal optimization tips
- Annual performance check

---

### PHASE 6: Long-Term Relationship

#### Annual Check-ins
```
[12 months after completion]

Bot: "🎂 One year anniversary!

Predicted: €1,150/year savings
Actual: €_____/year

To compare, upload this year's bills.

[Upload bills] [Skip check-in]

Typical results:
✅ 90-110% of predicted
⚠️ <85%: Tuning needed
🎉 >110%: Behavior bonus!"
```

#### Ongoing Value
- Monthly energy reports
- Benchmark vs similar homes
- New subsidy notifications
- Maintenance reminders
- Technology updates
- Community comparison

---

## TECHNICAL SPECIFICATIONS: WhatsApp Integration

### WhatsApp Business API Requirements

**Platform**: WhatsApp Business API
**AI Engine**: GPT-4 conversational AI
**Data Access**: Full plan from calculator
**Response Time**: <5 seconds typical
**Availability**: 24/7 automated
**Human Escalation**: Complex queries → human advisor
**Cost to User**: Free (unlimited messages)
**File Support**: PDF, images, spreadsheets
**Security**: End-to-end encrypted (WhatsApp standard)

### Bot Capabilities

**Natural Language Processing:**
- Dutch & English understanding
- Context retention (entire conversation)
- Intent detection
- Sentiment analysis

**Data Integration:**
- Live access to user's plan
- Contractor database
- Subsidy database (real-time)
- Energy price data

**Actions:**
- Generate documents (quotes, applications)
- Schedule appointments
- Send contractor requests
- Calculate custom scenarios
- Analyze uploaded documents (OCR)

**Automation:**
- Progress tracking
- Reminder scheduling  
- Status updates
- Performance monitoring

---

## USER DATA FLOW

```
1. CALCULATOR INPUT
   └─> Required fields + optional fields
   
2. ANALYSIS ENGINE
   └─> Processes all data
   
3. INITIAL PLAN OUTPUT
   └─> PDF/Excel/Web export
   
4. PHONE NUMBER ENTRY ⭐ NEW REQUIRED STEP
   └─> User provides WhatsApp number + consent
   
5. WHATSAPP BOT ACTIVATION
   └─> Bot receives complete plan data
   
6. CONVERSATIONAL GUIDANCE
   ├─> Questions answered
   ├─> Contractors matched
   ├─> Subsidies navigated
   └─> Work scheduled
   
7. IMPLEMENTATION TRACKING
   └─> Progress monitored
   
8. COMPLETION & BEYOND
   └─> Annual check-ins, ongoing optimization
```

---

## PRIVACY & CONSENT REQUIREMENTS

### Required Disclosures

**Before Phone Number Entry:**
- Clear explanation of WhatsApp bot purpose
- Privacy policy link (GDPR compliant)
- Data usage explanation
- Opt-out/unsubscribe process
- Contact data deletion rights

**Consent Checkbox Text:**
```
☐ I agree to receive personalized energy advice and 
  implementation guidance via WhatsApp. I understand:
  • My phone number will only be used for this service
  • Messages are free and unlimited
  • I can unsubscribe anytime by messaging "STOP"
  • My data is GDPR protected and never shared
  
  [Privacy Policy] [Terms of Service]
```

### Data Retention

**What's Stored:**
- Phone number (for WhatsApp delivery)
- Complete energy plan (for personalization)
- Conversation history (for context)
- Progress tracking data

**How Long:**
- Active users: Indefinitely (with consent)
- Unsubscribed: 30 days then deleted
- Inactive (12 months): Archived, can be deleted on request

**User Rights:**
- View all stored data (export)
- Delete account completely
- Opt-out anytime
- Update preferences

---

## BUSINESS VALUE PROPOSITION

### For Users:
- ❓ Complex decisions → Simple guidance
- 😰 Overwhelmed → Step-by-step support
- 🏢 Finding contractors → Vetted matches
- 📄 Confusing subsidies → Application help
- 📅 Coordination → Automated scheduling
- 📊 Verification → Continuous tracking

### Why It Works:
- No new app required
- Familiar platform (WhatsApp)
- Conversational interface
- Persistent (no lost progress)
- Proactive (reminders)
- Trusted (WhatsApp security)
- Accessible (24/7)

### Revenue Model:
- Free for users
- Contractor referral fees (when user requests quotes)
- Premium support tier (faster human response)
- White-label licensing (utilities, municipalities)

---

**Section Added**: Complete Workflow from Calculation → WhatsApp Bot
**Key Addition**: Phone number as required field for WhatsApp connection
**Bot Features**: Full conversational AI with plan integration
**Privacy**: GDPR compliant, explicit consent required
**Value**: Transforms static calculator into ongoing advisor service


---

## PART 4: CUSTOMIZABLE PLAN GENERATION

### Overview: From Initial Plan to YOUR Perfect Plan

After the calculator generates the initial plan, users can customize it through **multiple lenses** to match their specific situation, priorities, and constraints.

---

## CUSTOMIZATION DIMENSION 1: OPTIMIZATION STRATEGY

### User Selects Primary Goal (Required)

**Question Presented:**
```
🎯 What's your primary goal for this energy renovation?

Select your optimization strategy:
(Choose one that best matches your situation)
```

#### Strategy A: Maximum Savings (Default)
- **Focus**: Highest annual € savings
- **Prioritizes**: Improvements with biggest energy reduction
- **Best For**: High current bills, planning to stay long-term
- **Typical Result**: 50-70% energy reduction, 12-18 year payback
- **Example Priority Order**:
  1. Heat pump upgrade (saves €800/year)
  2. Wall insulation (saves €450/year)
  3. Floor heating extension (saves €320/year)
  4. Solar expansion (saves €280/year)

#### Strategy B: Fastest Payback (ROI Focused)
- **Focus**: Shortest payback period
- **Prioritizes**: Quick wins with low investment/high return
- **Best For**: Limited budget, want to see results fast
- **Typical Result**: 30-40% energy reduction, 3-7 year payback
- **Example Priority Order**:
  1. Smart thermostat (1.4 year payback)
  2. Air sealing (4.8 year payback)
  3. Attic insulation (8.2 year payback)
  4. Solar panels (8.5 year payback)

#### Strategy C: Budget Constrained
- **Focus**: Maximum impact within budget limit
- **Requires**: Budget limit input (€X,XXX)
- **Prioritizes**: Best € saved per € invested within constraint
- **Best For**: Fixed renovation budget, want optimal use
- **Typical Result**: Varies by budget, optimized selection
- **Example (€5,000 budget)**:
  1. Smart thermostat (€200)
  2. Air sealing (€1,200)
  3. Attic insulation (€2,500)
  4. Remaining: €1,100 toward wall insulation
  - Total saves: €480/year within €5K

#### Strategy D: Loan-Based Planning
- **Focus**: Affordable monthly payments
- **Requires**: Loan capacity, interest rate, term
- **Prioritizes**: Savings > loan payment ("cash flow positive")
- **Best For**: Financing renovation, want immediate net benefit
- **Typical Result**: Improvements where monthly savings exceed monthly payment
- **Example (€15K loan, 4% interest, 10 years)**:
  - Monthly payment: €152
  - Improvements generating >€152/month savings selected
  - Result: €180/month savings - €152 payment = €28/month net positive from day 1

#### Strategy E: Biggest Impact, Smallest Investment
- **Focus**: Maximum bang for buck (€ saved / € invested ratio)
- **Prioritizes**: Highest efficiency ratio improvements
- **Best For**: Strategic investor, wants proven high-ROI only
- **Typical Result**: Cherry-picks top 3-5 improvements with >15% ROI
- **Example Priority Order**:
  1. Smart thermostat (73% annual ROI)
  2. Air sealing (48% annual ROI)
  3. Attic insulation (24% annual ROI)
  - Stops before lower ROI items

#### Strategy F: Energy Label Target
- **Focus**: Achieve specific energy label
- **Requires**: Target label selection (e.g., "I want Label B")
- **Prioritizes**: Minimum investment to reach target label
- **Best For**: Selling home, mortgage requirement, personal goal
- **Typical Result**: Exact improvements needed for label, no more/less
- **Example (Current D → Target B)**:
  - Required: Wall insulation + Heat pump + Solar
  - Optional: Floor heating (would reach A, but exceeds target)
  - Investment: €14,200 (minimum for Label B)

#### Strategy G: DIY-Friendly Approach
- **Focus**: Maximize self-installation opportunities
- **Requires**: User skill level assessment
- **Prioritizes**: Improvements user can do themselves
- **Best For**: Handy homeowner, wants to save on labor
- **Typical Result**: Mix of DIY (60-70% labor savings) + professional
- **Example Priority Order**:
  1. Smart thermostat - DIY (save €150 labor)
  2. Air sealing - DIY (save €600 labor)
  3. Attic insulation - DIY possible (save €800 labor)
  4. Heat pump - Professional required
  - Total DIY savings: €1,550

#### Strategy H: Subsidy Maximization
- **Focus**: Maximize available government subsidies
- **Requires**: Subsidy database check
- **Prioritizes**: Currently subsidized improvements
- **Best For**: Taking advantage of limited-time programs
- **Typical Result**: Front-loads subsidized improvements before programs expire
- **Example (2025 subsidies)**:
  1. Heat pump (€3,500 ISDE subsidy) - Priority!
  2. Solar panels (0% BTW = 21% discount) - Priority!
  3. Insulation (Check gemeente subsidy)
  - Net investment: €11,200 instead of €16,400

#### Strategy I: Home Value Optimization
- **Focus**: Maximum home resale value increase
- **Requires**: Considering selling in 1-5 years
- **Prioritizes**: Visible improvements + energy label boost
- **Best For**: Planning to sell, want best return on investment
- **Typical Result**: Improvements buyers value most
- **Example Priority Order**:
  1. Energy label D→B (worth €8,000-€12,000)
  2. New windows (high buyer appeal)
  3. Solar panels (visible, attractive)
  4. Modern heating system (inspection appeal)
  - Skip: Attic insulation (invisible, less buyer impact)

---

## CUSTOMIZATION DIMENSION 2: FINANCIAL CONSTRAINTS

### Budget Settings (Optional but Highly Recommended)

#### Option 1: Fixed Budget
```
💰 What's your maximum budget?

Total available for energy improvements:
€ [_________]

[Examples: €5,000 | €15,000 | €30,000]

Calculator will optimize within this limit.
```

**How It Works:**
- Sorts improvements by ROI within budget
- Shows "what you get" at your budget level
- Indicates "what you'd miss" if budget increased
- Compares scenarios: Your budget vs +€5K vs +€10K

**Example Output (€10,000 budget):**
```
Within €10,000 budget:
✅ Smart thermostat (€200)
✅ Air sealing (€1,200)
✅ Attic insulation (€2,500)
✅ Solar panels (€6,000)
━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: €9,900
Annual savings: €725/year
Payback: 13.7 years
Label: D → D (still)

If budget was €15,000:
+ Wall insulation (€4,000)
= Label D → C, saves €1,050/year

If budget was €20,000:
+ Heat pump (€10,000)
= Label D → B, saves €1,480/year
```

---

#### Option 2: Loan-Based Financing
```
🏦 Financing this renovation with a loan?

Loan Details:
Max loan amount: € [_________]
Interest rate: [___]% per year
Loan term: [___] years

[Common: 4-6% interest, 5-15 year terms]

Calculator will ensure savings > payments.
```

**How It Works:**
- Calculates monthly loan payment
- Only recommends improvements where:
  - Monthly energy savings ≥ Monthly loan payment
  - Or: Payback period < Loan term
- Shows "cash flow positive" improvements

**Example Output (€15,000 loan, 4.5%, 10 years):**
```
Loan: €15,000 @ 4.5% for 10 years
Monthly payment: €155.67

Recommendations (savings > payment):
✅ Heat pump + Solar + Insulation
   Investment: €14,800
   Monthly savings: €180 (€95/month in savings)
   
   NET BENEFIT: €24/month cash flow positive
   
After 10 years (loan paid off):
   - You own all improvements
   - Full €180/month savings continues
   - Total 20-year benefit: €28,400

⚠️ Not recommended (savings < payment):
❌ Windows only (saves €85/month < €155 payment)
```

---

#### Option 3: Mortgage Integration
```
🏠 Refinancing or buying? 

Consider "Energiehypotheek" (Energy Mortgage):

Your situation:
○ New purchase with renovation
○ Refinancing existing mortgage
○ Green mortgage (better rate for energy label)

Current mortgage rate: [___]%
Potential energy mortgage rate: [___]%
   (Typically 0.1-0.3% lower for Label A/B)

Additional loan capacity for energy: € [_________]
```

**How It Works:**
- Calculates mortgage payment increase for improvements
- Compares energy savings vs payment increase
- Shows if label improvement qualifies for better mortgage rate
- Calculates long-term benefit including rate discount

**Example Output (Green Mortgage):**
```
Current mortgage: €300,000 @ 3.5% (30 years)
Monthly payment: €1,347

Option 1: Standard mortgage +€15K energy loan
Mortgage: €315,000 @ 3.5%
Payment: €1,414 (+€67/month)
Energy savings: €95/month
Net: €28/month benefit

Option 2: Green mortgage (Label A/B)
Mortgage: €315,000 @ 3.2% (0.3% discount)
Payment: €1,373 (+€26/month)
Energy savings: €95/month
Net: €69/month benefit ← BEST OPTION

Recommendation: Invest €15K to reach Label B
Benefit: €43/month better than standard loan!
20-year benefit: €10,320 extra savings
```

---

#### Option 4: Phased Investment (Staged Over Time)
```
📅 Prefer to spread improvements over time?

Investment timeline:
Year 1 budget: € [_________]
Year 2 budget: € [_________]
Year 3 budget: € [_________]

Calculator will create multi-year roadmap.
```

**How It Works:**
- Identifies dependencies (must do X before Y)
- Optimizes order across multiple years
- Shows cumulative savings building over time
- Accounts for energy price inflation

**Example Output (3-year phased plan):**
```
YEAR 1 (€5,000 budget):
1. Smart thermostat (€200)
2. Air sealing (€1,200)
3. Attic insulation (€2,500)
4. Budget buffer: €1,100
━━━━━━━━━━━━━━━━━━━━━━━━━━
Invested: €3,900
Saves: €420/year
Label: D → D (still)

YEAR 2 (€8,000 budget):
Uses Year 1 savings: €420 rollover
Total available: €8,420
5. Wall insulation (€4,000)
6. Solar panels (€4,000)
━━━━━━━━━━━━━━━━━━━━━━━━━━
Cumulative invested: €11,900
Saves: €950/year
Label: D → C

YEAR 3 (€10,000 budget):
Uses Year 1-2 savings: €1,370 rollover
Total available: €11,370
7. Heat pump (€10,000)
━━━━━━━━━━━━━━━━━━━━━━━━━━
Total invested: €21,900
Saves: €1,480/year
Label: D → B
Payback: 14.8 years

Benefits of phasing:
✅ Smaller annual budgets
✅ Earlier improvements start saving immediately
✅ Savings help fund later phases
✅ Can adjust plan based on results
```

---

## CUSTOMIZATION DIMENSION 3: IMPLEMENTATION PREFERENCES

### DIY Capability Assessment (Optional)

```
🔨 Can you do some work yourself?

Your skill level:
○ No DIY (hire everything)
○ Basic (painting, simple installs)
○ Intermediate (electrical, plumbing basics)
○ Advanced (major renovations)

Time available:
○ Weekends only
○ 1-2 weeks full time
○ Ongoing (spread over months)

Calculator will identify DIY opportunities.
```

**How It Works:**
- Tags each improvement: DIY Possible / Professional Required / Hybrid
- Estimates labor savings if done DIY
- Provides skill requirements and time estimates
- Links to DIY guides and tutorials

**Example Output (Intermediate skill level):**
```
DIY OPPORTUNITIES IDENTIFIED:

✅ CAN DIY (Save €1,950 in labor):
1. Smart thermostat
   Skill: Basic
   Time: 2-3 hours
   Labor savings: €150
   [Video tutorial] [Installation guide]

2. Air sealing
   Skill: Basic
   Time: 1-2 days
   Labor savings: €600
   Materials: €600, You save labor
   [Complete DIY guide]

3. Attic insulation
   Skill: Intermediate
   Time: 2-3 days
   Labor savings: €800
   ⚠️ Note: Heavy materials, 2 people recommended
   [Safety guide] [Step-by-step]

4. Pipe insulation
   Skill: Basic
   Time: 3-4 hours
   Labor savings: €200
   [Quick guide]

⚠️ REQUIRES PROFESSIONAL:
- Heat pump (€10,000 + €1,800 install)
  Reason: Gas connection, permits, warranty
  
- Solar panels (€6,000 + €800 install)
  Reason: Roof safety, electrical certification

- Wall insulation (€3,200 + €800 install)
  Reason: Special equipment needed

HYBRID OPTIONS (Save ~50%):
- Floor heating: Pro for system, DIY for floor prep
  Normal: €4,500 all-in
  Hybrid: €3,200 (you prep, pro installs system)

YOUR DIY PLAN:
Do yourself: Smart thermostat, air sealing, attic
Hire: Heat pump, solar, wall insulation
Total savings: €1,550 in labor costs
Your time investment: 4-5 days work
```

---

### Subsidy Optimization (Automatic)

```
💰 Subsidy Check (Automatic)

The calculator automatically checks for:
✓ ISDE (National subsidies)
✓ BTW korting (VAT reduction)
✓ Gemeente subsidies (Local programs)
✓ Energy company rebates
✓ Green mortgage discounts

Found applicable subsidies: [X programs]
```

**How It Works:**
- Checks each improvement against subsidy database
- Calculates net cost after subsidies
- Flags time-limited programs (apply soon!)
- Provides application guidance
- Updates investment amounts automatically

**Example Output:**
```
SUBSIDIES FOUND (€5,700 total):

✅ Heat Pump
ISDE Subsidy: €3,500
• Application: Before installation
• Installer: Must be RVO-registered
• Timeline: 4-6 weeks approval
• Valid until: Dec 31, 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━
Gross cost: €10,000
Net cost: €6,500 ← SUBSIDIZED

✅ Solar Panels
0% BTW (VAT exemption): €1,400 savings
• Automatic: Invoice shows 0% BTW
• No application needed
• Valid: Indefinitely (2023+ policy)
━━━━━━━━━━━━━━━━━━━━━━━━━━
Gross cost: €8,000
Net cost: €6,600 ← TAX SAVINGS

⚠️ Wall Insulation
Gemeente Amsterdam: Up to €800
• Application: Before installation
• Deadline: June 30, 2025 (4 months!)
• Budget: Limited, first-come basis
• Apply now: [Link to application]
━━━━━━━━━━━━━━━━━━━━━━━━━━
Gross cost: €4,000
Net cost: €3,200 ← IF APPROVED

❌ Windows
No subsidies currently available
Gross cost: €7,000
Net cost: €7,000 (no subsidy)

━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL IMPACT:
Before subsidies: €29,000
After subsidies: €23,300
YOU SAVE: €5,700 (19.7% discount!)

⏰ ACTION REQUIRED:
1. ISDE heat pump (apply before installation)
2. Gemeente insulation (deadline in 4 months!)

Calculator has adjusted all costs to show
net amounts after available subsidies.
```

---

### Mortgage Rate Discount (Energy Label Based)

```
🏦 Green Mortgage Benefits

If improving energy label:
Current label: D
Target label: B
Potential mortgage discount: 0.2-0.3%

Your situation:
Mortgage amount: € [_________]
Current rate: [___]%
Improved label rate: [___]%

Calculate benefit:
```

**How It Works:**
- Checks if label improvement qualifies for green mortgage
- Calculates monthly payment difference
- Shows lifetime interest savings
- Compares: Energy improvement cost vs mortgage savings

**Example Output:**
```
GREEN MORTGAGE ANALYSIS:

Current Situation:
Mortgage: €300,000 @ 3.5% (30 years)
Monthly: €1,347
Total interest: €184,968

After Label D → B Improvement:
Mortgage: €300,000 @ 3.2% (30 years)
Monthly: €1,301 (-€46/month)
Total interest: €168,360

MORTGAGE SAVINGS:
Monthly: €46
Annually: €552
30-year total: €16,608 interest saved

INVESTMENT FOR LABEL B:
Heat pump + Insulation + Solar: €14,800
(after subsidies)

COMPLETE ROI PICTURE:
Energy savings: €1,150/year
Mortgage savings: €552/year
━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL BENEFIT: €1,702/year

Investment: €14,800
Payback: 8.7 years ← EXCELLENT!

Without mortgage discount:
Payback would be 12.9 years

Mortgage discount adds €16,608 value!

✅ RECOMMENDATION: Energy improvements
are even better deal with green mortgage.
```

---

## CUSTOMIZATION DIMENSION 4: PRIORITY SYSTEM

### Impact vs Investment Matrix

```
📊 How do you want to prioritize?

Select your priority formula:

○ Biggest impact first (€ saved, regardless of cost)
○ Smallest investment first (build momentum)
○ Best ratio first (€ saved / € invested)
○ Critical path first (unlock other improvements)
○ Subsidy-driven (use programs before they expire)
○ DIY-first (do yourself now, hire later)
○ Label-focused (achieve target label)
```

**Priority A: Biggest Impact First**
- Sorts by: Annual € savings (descending)
- Logic: "Do the thing that saves the most money"
- Result: Large investments upfront
```
1. Heat pump: €800/year savings
2. Wall insulation: €450/year
3. Floor heating: €320/year
4. Solar: €280/year
```

**Priority B: Smallest Investment First**
- Sorts by: Investment amount (ascending)
- Logic: "Build momentum with quick wins"
- Result: Many small improvements first
```
1. Smart thermostat: €200
2. Air sealing: €1,200
3. Attic insulation: €2,500
4. Solar panels: €6,600
```

**Priority C: Best Ratio First (ROI)**
- Sorts by: Annual savings ÷ Investment
- Logic: "Most efficient use of money"
- Result: Highest return-on-investment improvements
```
1. Smart thermostat: 73% annual ROI
2. Air sealing: 48% annual ROI
3. Attic insulation: 24% annual ROI
4. Solar panels: 18% annual ROI
```

**Priority D: Critical Path (Dependencies)**
- Sorts by: System dependencies
- Logic: "Do foundation improvements that unlock others"
- Result: Logical installation sequence
```
1. Floor heating first (enables heat pump efficiency)
2. Heat pump second (now works optimally)
3. Insulation third (reduces heat pump load)
4. Solar last (sized correctly after usage drops)
```

**Priority E: Subsidy-Driven**
- Sorts by: Subsidy amount + deadline urgency
- Logic: "Use limited programs before they expire"
- Result: Time-sensitive opportunities first
```
1. Heat pump (€3,500 subsidy, ends Dec 2025) ← URGENT
2. Gemeente insulation (€800, deadline June) ← URGENT
3. Solar (0% BTW, indefinite) ← AVAILABLE
4. Windows (no subsidy) ← LAST
```

**Priority F: DIY-First**
- Sorts by: DIY feasibility
- Logic: "Do what I can now, hire pros later"
- Result: Self-installation opportunities first
```
1. Smart thermostat (DIY, 2 hours)
2. Air sealing (DIY, 2 days)
3. Attic insulation (DIY possible, 3 days)
4. Heat pump (Professional required) ← LATER
```

**Priority G: Label-Focused**
- Sorts by: Label point contribution
- Logic: "Achieve target label with minimum cost"
- Result: Only improvements needed for target
```
Target: Label B (currently D)

Required for Label B:
✅ Wall insulation (+0.8 label points)
✅ Heat pump (+0.9 label points)
✅ Solar panels (+0.4 label points)
= Total: +2.1 points = Label B achieved

NOT needed for Label B:
❌ Floor heating (would reach A, exceeds target)
❌ Windows (not enough impact for cost)

Minimum investment: €14,200 for Label B
```

---

## PLAN COMPARISON: SIDE-BY-SIDE SCENARIOS

### Compare Multiple Strategies Simultaneously

```
📊 Compare Your Options

The calculator shows multiple plans side-by-side:

                │ Quick Wins │ Balanced  │ Complete
━━━━━━━━━━━━━━━━│━━━━━━━━━━━│━━━━━━━━━━│━━━━━━━━━
Investment      │ €4,100     │ €14,800   │ €24,300
Annual Savings  │ €420       │ €1,150    │ €1,680
Payback         │ 9.8 years  │ 12.9 yrs  │ 14.5 yrs
Energy Label    │ D → D      │ D → B     │ D → A
Home Value      │ +€0        │ +€10,000  │ +€18,000
DIY Possible    │ 100%       │ 40%       │ 25%
Subsidies       │ €0         │ €5,700    │ €7,900
Loan Payment*   │ €67/mo     │ €180/mo   │ €294/mo
Net Cash Flow*  │ -€32/mo    │ +€15/mo   │ +€46/mo

*Based on 4.5% loan, 10 years

[Select: Quick Wins] [Select: Balanced] [Select: Complete]
[Create Custom Plan]
```

---

## INTERACTIVE PLAN EDITOR

### Drag-and-Drop Customization

Users can manually adjust the plan:

```
YOUR CUSTOM PLAN

Drag improvements to reorder priority
Toggle on/off with checkbox
Edit costs with actual quotes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☑ 1. Smart Thermostat           €200    [↕]
      Annual savings: €145
      Payback: 1.4 years
      [Edit cost] [Remove] [Details]
      
☑ 2. Attic Insulation         €2,500    [↕]
      Annual savings: €280
      Payback: 8.9 years
      [Edit cost] [Remove] [Details]
      
☐ 3. Wall Insulation          €4,000    [↕]
      Annual savings: €450
      Payback: 8.9 years
      [Edit cost] [Remove] [Details]
      
☑ 4. Heat Pump               €10,000    [↕]
      Annual savings: €800
      Requires: Floor heating (see below)
      ⚠️ Limited efficiency without floor heating
      [Edit cost] [Remove] [Details]

[+ Add Custom Improvement]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOTALS (Selected items):
Investment: €12,700
Annual Savings: €1,225
Payback: 10.4 years
Label: D → C

[Save Custom Plan] [Export] [Send to WhatsApp]
```

---

## CONSTRAINT-BASED PLANNING

### The Calculator Enforces:

**Technical Dependencies:**
```
⚠️ DEPENDENCY DETECTED:

You selected: Heat Pump (€10,000)
Requires: Floor heating or low-temp radiators

Your home: 60% radiators, 40% floor heating

Options:
1. Add floor heating extension (€4,500)
   → Full heat pump efficiency
   
2. Upgrade to low-temp radiators (€2,800)
   → Good heat pump efficiency
   
3. Proceed with hybrid (floor heating only in some rooms)
   → Reduced heat pump efficiency (-25%)

[Add floor heating] [Upgrade radiators] [Accept hybrid]
```

**Budget Constraints:**
```
⚠️ BUDGET EXCEEDED:

Your budget: €10,000
Current selection: €12,700
Over by: €2,700

Suggestions to fit budget:
1. Remove: Wall insulation (-€4,000)
   New total: €8,700 ✓ Under budget
   
2. Replace: Heat pump → HR++ boiler
   Saves: €6,500, New total: €6,200 ✓
   
3. Phase: Move wall insulation to Year 2
   Year 1: €8,700 ✓ Fits budget

[Auto-optimize to budget] [Manual adjustments]
```

**Subsidy Timing:**
```
⏰ SUBSIDY DEADLINE ALERT:

Heat pump ISDE subsidy (€3,500)
Application deadline: June 30, 2025
Days remaining: 87 days

To qualify:
✓ Apply before installation
✓ Use RVO-registered installer
✓ Complete within 6 months of approval

Recommendation:
Move heat pump to Phase 1 (immediate)
to capture subsidy before deadline.

[Adjust timeline] [View application process]
```

---

## ADVANCED: LOAN SCENARIO CALCULATOR

### Detailed Financing Analysis

```
💳 LOAN SCENARIO PLANNER

Investment needed: €15,000

OPTION 1: Personal Loan
Amount: €15,000
Rate: 6.5% APR
Term: 7 years
Payment: €233/month
Total interest: €4,572

OPTION 2: Home Equity Loan  
Amount: €15,000
Rate: 4.2% APR
Term: 10 years
Payment: €153/month
Total interest: €3,360

OPTION 3: Energy Mortgage (Refinance)
Add to mortgage: €15,000
Rate: 3.2% (green mortgage discount)
Term: 30 years
Payment increase: €63/month
Total interest: €7,680*
*But spread over 30 years

OPTION 4: Phased (No Loan)
Year 1: Save €5,000 + do €5,000 improvements
Year 2: Use savings + add €5,000 more
Year 3: Complete with accumulated savings
Total interest: €0

Energy Savings: €95/month

NET MONTHLY CASH FLOW:
Option 1: €95 - €233 = -€138/month ❌
Option 2: €95 - €153 = -€58/month ❌
Option 3: €95 - €63 = +€32/month ✅ POSITIVE
Option 4: Varies by phase

RECOMMENDATION: Option 3 (Green Mortgage)
✓ Positive cash flow from day 1
✓ Lowest rate (green discount)
✓ Long term = low payment
✓ Can pay extra if desired

[Apply for green mortgage] [Compare more options]
```

---

## SUMMARY: CUSTOMIZATION FLOWCHART

```
1. SELECT OPTIMIZATION STRATEGY
   ├─ Maximum Savings
   ├─ Fastest Payback
   ├─ Budget Constrained
   ├─ Loan-Based
   ├─ Biggest Impact/Smallest Investment
   ├─ Energy Label Target
   ├─ DIY-Friendly
   ├─ Subsidy Maximization
   └─ Home Value Optimization
   
2. SET FINANCIAL PARAMETERS
   ├─ Fixed Budget (€X)
   ├─ Loan Details (amount, rate, term)
   ├─ Mortgage Integration (green mortgage)
   └─ Phased Timeline (multi-year)
   
3. SPECIFY PREFERENCES
   ├─ DIY Capability (skill level)
   ├─ Priority System (impact/cost/ratio)
   └─ Constraints (timeline, disruption)
   
4. AUTO-APPLY
   ├─ Available Subsidies
   ├─ Technical Dependencies
   └─ Mortgage Rate Discounts
   
5. GENERATE CUSTOM PLAN
   └─ Optimized for YOUR situation
   
6. REVIEW & ADJUST
   ├─ Compare Scenarios
   ├─ Edit Manually
   └─ Run "What-If" Analysis
   
7. FINALIZE & EXPORT
   ├─ PDF Report
   ├─ Implementation Timeline
   └─ Send to WhatsApp Bot for Guidance
```

---

## WHAT-IF ANALYSIS TOOL

### Real-Time Scenario Testing

```
🔄 WHAT-IF CALCULATOR

Test different scenarios instantly:

What if...

Energy prices increase 20%?
Current plan payback: 12.9 years
With 20% price increase: 9.7 years ✓
Recommendation: Invest sooner

I get a €5,000 inheritance?
Current: Phased over 3 years
With extra €5,000: Complete in Year 1
Benefit: €840 extra savings from earlier completion

I do attic insulation myself?
Professional: €2,500 total
DIY: €1,700 (save €800 labor)
Payback: 8.9 → 6.1 years
Recommendation: Consider DIY if capable

My mortgage rate is 0.3% lower (green)?
Current 30-year cost: €184,968
With green discount: €168,360
Saves: €16,608 in interest
Recommendation: Energy improvements pay for themselves!

I wait 2 years to start?
Lost savings: €2,300 (€1,150 × 2)
Subsidy risk: ISDE may change
Recommendation: Start sooner if possible

[Run custom scenario] [Compare results]
```

---

**Section Added**: Complete Plan Customization Framework
**Key Features**: 
- 9 optimization strategies
- 4 financing models (budget/loan/mortgage/phased)
- DIY capability integration
- Automatic subsidy optimization
- Green mortgage discount calculations
- Interactive plan editor
- Constraint enforcement
- What-if analysis tool
- Side-by-side scenario comparison

**Result**: Users can create a plan perfectly matched to their situation, priorities, and constraints.


---

## PART 5: COMPREHENSIVE MORTGAGE BENEFITS ANALYSIS

### Overview: Hidden Financial Benefits of Energy Improvements

Energy improvements create **three separate mortgage-related benefits** that are often overlooked but can dramatically improve the financial case for renovation:

1. **Home Value Increase** → Lower LTV (Loan-to-Value) ratio
2. **Energy Label Improvement** → Qualify for green mortgage rates
3. **Combined Effect** → Potential refinancing opportunity

---

## MORTGAGE BENEFIT 1: HOME VALUE INCREASE & LTV IMPROVEMENT

### How Energy Improvements Increase Home Value

#### Value Increase by Energy Label

**Netherlands Market Data (2024-2025):**
```
Label Improvement    │ Typical Value Increase
─────────────────────│──────────────────────────
G → F               │ +€3,000 - €5,000
F → E               │ +€4,000 - €6,000
E → D               │ +€5,000 - €8,000
D → C               │ +€6,000 - €10,000
C → B               │ +€8,000 - €12,000
B → A               │ +€10,000 - €15,000
A → A+/A++          │ +€12,000 - €20,000

Multi-step improvements:
E → C (skip D)      │ +€11,000 - €18,000
E → B (skip D, C)   │ +€19,000 - €30,000
D → A (skip C, B)   │ +€24,000 - €37,000
```

**Regional Variations:**
- **Amsterdam/Utrecht**: +15-25% above average
- **Rotterdam/The Hague**: +10-15% above average
- **Rural areas**: -10-20% below average
- **Student cities**: +20-30% for efficiency (Groningen, Wageningen)

---

### LTV (Loan-to-Value) Ratio Impact

#### Required Input Fields for LTV Analysis:

```
🏠 MORTGAGE & HOME VALUE DETAILS

Current Mortgage Information:
Outstanding mortgage balance: € [_________]
Original purchase price: € [_________]
Purchase year: [____]
Current estimated home value: € [_________]
   (Or auto-estimate based on address)

Energy Improvements Impact:
Calculator will estimate new home value after
energy label improvement.
```

#### How It Works:

**BEFORE Energy Improvements:**
```
Home value: €350,000
Mortgage: €280,000
LTV ratio: 80% (€280,000 ÷ €350,000)
```

**AFTER Energy Improvements (Label D → B):**
```
Home value: €350,000 + €10,000 = €360,000
Mortgage: €280,000 (unchanged)
LTV ratio: 77.8% (€280,000 ÷ €360,000)

LTV improvement: 2.2 percentage points
```

---

### LTV Improvement Benefits:

#### Benefit 1A: Lower Monthly Mortgage Insurance (if LTV was >80%)

**Before (LTV 85%):**
```
Mortgage: €300,000
LTV: 85%
Mortgage Insurance (NHG alternative): €125/month
Annual cost: €1,500
```

**After Improvement + Value Increase:**
```
Mortgage: €300,000
Home value: €340,000 → €353,000
New LTV: 85% → 84.9%

Still requires insurance, but:
Lower risk tier: €110/month
Annual savings: €180/year
```

**After hits 80% threshold:**
```
LTV reaches 80% or below
Insurance: Not required
Annual savings: €1,500/year
```

---

#### Benefit 1B: Refinancing Opportunities at Better Rates

**LTV-Based Rate Tiers (Netherlands 2025):**
```
LTV Range       │ Typical Interest Rate
────────────────│──────────────────────
≤ 60% LTV       │ 3.0% - 3.3% (best rates)
60-70% LTV      │ 3.2% - 3.5%
70-80% LTV      │ 3.4% - 3.8%
80-90% LTV      │ 3.6% - 4.2%
90-100% LTV     │ 3.9% - 4.8%
> 100% LTV      │ 4.5%+ (if allowed)
```

**Example Refinancing Scenario:**

**Original Situation:**
```
Purchase price: €340,000
Mortgage: €300,000 (88% LTV)
Rate: 4.1% (high LTV penalty)
Monthly: €1,447
```

**After 3 Years + Energy Improvements:**
```
Remaining mortgage: €290,000
Home value: €360,000 (market +€10K + improvements +€10K)
New LTV: 80.6% (just above tier break)

Option: Pay down €3,000 to reach 80% LTV
New mortgage: €287,000
New LTV: 79.7%
New rate: 3.6% (better tier)
New monthly: €1,315

Monthly savings: €132/month
Annual savings: €1,584/year

Cost to achieve:
€3,000 principal payment
Payback: 1.9 years from interest savings alone
```

---

## MORTGAGE BENEFIT 2: GREEN MORTGAGE RATES (ENERGY LABEL BASED)

### Banks Offering Green Mortgage Discounts (Netherlands)

#### Current Programs (2025):

```
Bank/Lender          │ Label Required │ Rate Discount
─────────────────────│────────────────│──────────────
ABN AMRO             │ A or better    │ -0.30%
ING                  │ A or B         │ -0.25%
Rabobank             │ A, B, or C     │ -0.20%
ASN Bank             │ B or better    │ -0.35%
Triodos Bank         │ B or better    │ -0.30%
SNS/RegioBank        │ A or better    │ -0.25%
Obvion               │ A or B         │ -0.20%
Florius              │ A, B, or C     │ -0.15%
Nationale Hypotheek  │ A or better    │ -0.28%

Average Discount: 0.25% for Label B
              0.30% for Label A
```

---

### Required Input Fields for Green Mortgage Analysis:

```
💚 GREEN MORTGAGE QUALIFICATION

Current Mortgage Details:
Current interest rate: [___]% per year
Remaining term: [___] years
Fixed period end date: [MM/YYYY]
Mortgage type: 
  ○ Linear (annuïteit)
  ○ Interest-only (aflossingsvrij)
  ○ Hybrid

Refinancing Considerations:
Early repayment penalty: € [_________]
   (Or percentage of remaining balance)
Remaining fixed period: [___] months
Break costs estimated: € [_________]

New Mortgage Rate (with green discount):
Target energy label after improvements: [___]
Estimated green mortgage rate: [___]%
   (Calculator auto-fills based on current market)
```

---

### Green Mortgage Benefit Calculation:

#### Example 1: Immediate Refinancing

**Current Situation:**
```
Mortgage: €300,000
Rate: 3.8% (fixed until 2025, ending soon)
Term: 30 years remaining
Monthly: €1,398
```

**After Energy Improvement (Label D → B):**
```
Qualifies for: Green mortgage discount
New rate: 3.55% (3.8% - 0.25% discount)
New monthly: €1,360
Monthly savings: €38/month
Annual savings: €456/year
30-year savings: €13,680 total interest
```

**ROI Calculation:**
```
Energy improvements cost: €14,800
Annual energy savings: €1,150
Annual mortgage savings: €456
TOTAL annual benefit: €1,606/year

Payback period: 9.2 years (vs 12.9 without mortgage benefit)

Additional value: €13,680 interest saved over 30 years
```

---

#### Example 2: Refinancing with Break Costs

**Current Situation:**
```
Mortgage: €280,000
Current rate: 2.5% (locked until 2028)
Remaining fixed period: 36 months
Early repayment penalty: €8,400
```

**Calculation:**
```
New green rate available: 3.2% - 0.3% = 2.9%

Wait... 2.9% > 2.5% current rate!

RECOMMENDATION: Don't refinance yet.

Better strategy:
1. Complete energy improvements now
2. Start saving immediately on energy bills
3. Obtain energy label certificate
4. When fixed period ends (2028), refinance to green rate
5. By 2028, rates may be different, but you qualify for discount

Annual energy savings (start now): €1,150
Wait 3 years, save: €3,450
Then add mortgage discount when refinancing
```

**Smart Planning:**
```
This example shows importance of timing:
✓ Do energy improvements now (start saving)
✗ Don't refinance if current rate better
✓ Get label certificate (ready when needed)
✓ Refinance to green mortgage when fixed period ends
```

---

#### Example 3: New Purchase with Green Mortgage

**Scenario: Buying a home that needs energy improvements**

**Purchase Details:**
```
Purchase price: €375,000
Down payment: €75,000 (20%)
Mortgage needed: €300,000
Current label: E
```

**Option A: Standard Mortgage**
```
Mortgage: €300,000
LTV: 80%
Standard rate: 3.7%
Monthly: €1,383
```

**Option B: Include Renovation + Green Mortgage**
```
Purchase price: €375,000
Renovation cost: €15,000 (energy improvements)
Total: €390,000

Down payment: €75,000
Mortgage needed: €315,000

BUT: After improvements
Home value: €375,000 + €10,000 = €385,000
LTV: 81.8% (slightly higher, but...)
Label: E → B (qualifies for green rate!)

Green mortgage rate: 3.4% (0.3% discount)
Monthly: €1,394 (+€11 vs option A)

BENEFIT ANALYSIS:
Extra mortgage: €11/month
Energy savings: €95/month
NET BENEFIT: €84/month from day 1!

Plus: Home worth €10,000 more immediately
```

**Why Option B is Better:**
```
Standard mortgage: 
  - Lower rate (3.7%)
  - But need energy renovation anyway
  - Pay for it out of pocket later

Green mortgage:
  - Slightly higher rate vs standard (3.4%)
  ✓ But includes renovation in mortgage
  ✓ Immediate energy savings
  ✓ Home value increase
  ✓ Better LTV in 5 years
  ✓ Lower total cost of ownership

Total 30-year benefit: €30,000+
```

---

## MORTGAGE BENEFIT 3: COMBINED LTV + LABEL BENEFITS

### The Multiplicative Effect

When home value increases AND you qualify for green mortgage rates, the benefits multiply:

#### Triple Benefit Scenario:

**Starting Position:**
```
Home value: €340,000
Mortgage: €290,000
LTV: 85.3%
Rate: 4.0% (higher due to LTV >80%)
Label: D
Monthly payment: €1,380
```

**After Energy Improvements (€15,000 invested):**
```
BENEFIT 1: Home Value Increase
Label D → B = +€10,000 value
New home value: €350,000
New LTV: 82.9% (still >80%)

BENEFIT 2: Energy Savings
Annual savings: €1,150

BENEFIT 3: Pay Tiny Extra to Cross LTV Threshold
Current LTV: 82.9% (€290K / €350K)
Need to reach: 80% LTV = €280,000 mortgage
Additional paydown: €10,000

New LTV: 80.0%
Qualifies for: Better rate tier (3.7% vs 4.0%)

BENEFIT 4: Green Mortgage Discount
Label B qualifies for: -0.25% discount
Final rate: 3.45% (3.7% - 0.25%)

NEW MONTHLY PAYMENT: €1,248
Old payment: €1,380
Monthly savings: €132
Annual savings: €1,584/year
```

**Complete ROI Analysis:**
```
INVESTMENTS:
Energy improvements: €15,000
LTV paydown: €10,000
TOTAL: €25,000

ANNUAL BENEFITS:
Energy savings: €1,150
Mortgage interest savings: €1,584
TOTAL: €2,734/year

PAYBACK PERIOD: 9.1 years

ONE-TIME BENEFITS:
Home value increase: €10,000
Effective net investment: €15,000

LONG-TERM (remaining 25 years):
Mortgage interest saved: €39,600
Energy costs saved: €28,750
TOTAL BENEFIT: €68,350

ROI: 173% over life of mortgage
```

---

## MORTGAGE BENEFIT 4: SPECIAL PROGRAMS & EXEMPTIONS

### National Mortgage Guarantee (NHG) - Energy Exemption

```
📋 NHG ENERGY EXEMPTION

Standard NHG Limit (2025): €435,000
Energy Improvement Exemption: +€30,000
Maximum with energy improvements: €465,000

Qualification:
✓ Must improve energy label by 2+ steps
✓ Improvements must be ≤€30,000
✓ Must be documented in quote
✓ Work completed within 12 months

Benefits:
✓ 0.6% lower interest rate (typical)
✓ Protection if unable to pay
✓ Better terms overall
```

**Example:**
```
Purchase price: €445,000
Standard: Exceeds NHG limit (€435K), no guarantee

With energy improvements:
Purchase: €445,000
Planned energy work: €25,000
Total: €470,000

BUT: Energy exemption allows €465,000
Solution: €20,000 down payment
Mortgage: €450,000 with NHG

Benefits:
✓ NHG protection
✓ 0.6% better rate
✓ On €450K = €2,700/year savings
```

---

## REQUIRED INPUT FIELDS: COMPLETE MORTGAGE ANALYSIS

### New Input Fields Needed:

```
🏦 COMPREHENSIVE MORTGAGE ANALYSIS

Section A: Current Mortgage
Outstanding balance: € [_________]
Current interest rate: [___]% per year
Remaining term: [___] years
Monthly payment: € [_________]
Fixed period ends: [MM/YYYY]
Mortgage type: [Linear/Interest-only/Hybrid]

Section B: Home Value
Original purchase price: € [_________]
Purchase year: [____]
Current market value: € [_________]
   ○ I know the value
   ○ Auto-estimate from address
   ○ Recent appraisal (upload)

Current LTV ratio: [Auto-calculated]

Section C: Refinancing Potential
Early repayment allowed: [Yes/No]
Early repayment penalty: € [_________]
   or [___]% of remaining balance
Break costs if refinancing now: € [_________]

Section D: Green Mortgage Interest
Are you currently on green mortgage: [Yes/No]
Target energy label: [Select: A++/A+/A/B/C/D/E/F/G]
Current label: [Auto-filled from earlier input]

Section E: Future Plans
Plan to sell home: [Within 1-5 years / 5-10 years / 10+ years / Never]
Plan to refinance: [Yes, when fixed ends / Yes, ASAP / No plans / Unsure]
Can make extra payment: € [_________] available for LTV improvement
```

---

## MORTGAGE BENEFITS CALCULATOR OUTPUT

### What User Sees:

```
💰 COMPLETE MORTGAGE BENEFITS ANALYSIS

Your Current Situation:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Home value: €340,000
Mortgage: €290,000
LTV: 85.3%
Rate: 4.0%
Monthly payment: €1,380
Energy label: D
Annual energy cost: €3,240

After Energy Improvements:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BENEFIT 1: HOME VALUE INCREASE
Label D → B improvement
Market value increase: +€10,000
New home value: €350,000
New LTV: 82.9% (2.4 points better!)

BENEFIT 2: ENERGY COST SAVINGS
Annual savings: €1,150/year
20-year total: €23,000

BENEFIT 3: GREEN MORTGAGE QUALIFICATION
You qualify for green mortgage!
Available discount: -0.25% rate
From: 4.0% → To: 3.75%

BENEFIT 4: LTV IMPROVEMENT OPPORTUNITY
Optional: Pay extra €10,000 to reach 80% LTV
Unlocks: Additional -0.25% rate reduction
Combined rate: 3.5% (from 4.0%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATION: STRATEGY 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Strategy 1: Energy Improvements Only
Investment: €15,000
Monthly savings: €95 (energy)
Payback: 13.2 years

Strategy 2: Energy + Refinance (Green Rate) ✓ BEST
Investment: €15,000 (energy)
New rate: 3.75%
Monthly savings: €95 (energy) + €92 (mortgage)
Total: €187/month
Payback: 6.7 years
30-year benefit: €67,320

Strategy 3: Energy + LTV Improvement + Refinance
Investment: €15,000 (energy) + €10,000 (principal)
New rate: 3.5%
Monthly savings: €95 (energy) + €183 (mortgage)
Total: €278/month
Payback: 7.5 years
30-year benefit: €100,080 ← MAXIMUM BENEFIT

Strategy 4: Wait for Fixed Period to End (2028)
Do energy now: Save €1,150/year immediately
Wait to refinance: 36 months
Then apply green rate: Save mortgage cost from 2028
Total benefit: €3,450 (energy) + future mortgage savings

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PERSONALIZED RECOMMENDATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Based on your fixed period ending in 3 months:

✅ DO NOW:
1. Complete energy improvements (€15,000)
2. Obtain new energy label certificate
3. Apply for green mortgage refinancing
4. Consider €10K extra payment for 80% LTV

FINANCIAL IMPACT:
Immediate: €187/month benefit (energy + mortgage)
3-year: €6,732 cumulative savings
30-year: €67,320 total benefit

TIMELINE:
Month 1: Start energy improvements
Month 2: Complete work, get label
Month 3: Apply for green mortgage
Month 4: Refinance to 3.75% rate
Month 5: Start saving €187/month

[Download Detailed Analysis PDF]
[Compare All Strategies]
[Send to WhatsApp for Guidance]
```

---

## MORTGAGE BENEFITS: STRATEGY COMPARISON TABLE

```
┌─────────────────────────────────────────────────────────────────────┐
│           MORTGAGE STRATEGY COMPARISON                              │
├─────────────┬──────────┬──────────┬──────────┬─────────────────────┤
│ Strategy    │ Invest   │ New Rate │ Monthly  │ 30-Year Benefit     │
├─────────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ Do Nothing  │ €0       │ 4.0%     │ €0       │ €0                  │
│ (Baseline)  │          │          │          │ (keep paying high)  │
├─────────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ Energy Only │ €15,000  │ 4.0%     │ +€95     │ €34,200             │
│             │          │(no change)│ (energy) │ (energy only)       │
├─────────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ Green       │ €15,000  │ 3.75%    │ +€187    │ €67,320             │
│ Mortgage    │          │ (0.25%   │ (both)   │ (energy+mortgage)   │
│             │          │ discount)│          │                     │
├─────────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ Green +     │ €25,000  │ 3.5%     │ +€278    │ €100,080            │
│ LTV to 80%  │(€10K more│ (0.5%    │ (both)   │ (energy+mortgage)   │
│             │ paydown) │ total    │          │                     │
│             │          │ discount)│          │                     │
├─────────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ Wait Then   │ €15,000  │ 4.0% →   │ +€95 now │ €3,450 (3 yrs) +    │
│ Refinance   │ (3 years)│ 3.75%    │ +€187    │ €51,732 (27 yrs)    │
│             │          │ (in 2028)│ later    │ = €55,182 total     │
└─────────────┴──────────┴──────────┴──────────┴─────────────────────┘

BEST CHOICE DEPENDS ON:
• Fixed period remaining (break costs vs. savings)
• Available cash (€15K vs €25K)
• Time horizon (staying how long?)
• Risk tolerance (lock in savings now vs. wait)
```

---

## ADVANCED: MORTGAGE OPTIMIZATION CALCULATOR

### Interactive Scenario Planning:

```
🎯 MORTGAGE OPTIMIZATION TOOL

Adjust sliders to see impact:

Energy Investment: €[====€15,000====] €0 - €30,000
Extra Principal:   €[===€10,000=====] €0 - €50,000
New Rate:          [====3.5%========] 2.5% - 5.0%
                   (Auto: based on LTV + Green discount)

LIVE RESULTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current monthly: €1,380
New monthly: €1,102 (-€278)

Annual savings: €3,336
  ├─ Energy: €1,150
  └─ Mortgage: €2,186

Total investment: €25,000
Payback period: 7.5 years

30-year total benefit: €100,080
  ├─ Energy savings: €34,500
  ├─ Interest saved: €65,580
  └─ Home value increase: €10,000 (one-time)

New LTV: 80.0% (from 85.3%)
New home equity: €70,000 (from €50,000)

[Save This Scenario] [Compare to Others] [Export PDF]
```

---

**Section Added**: Comprehensive Mortgage Benefits Analysis
**Key Features**:
- Home value increase calculations (by label)
- LTV improvement analysis (with bank tier rates)
- Green mortgage discount (bank-by-bank rates)
- Combined LTV + Green rate benefits
- NHG energy exemption
- Refinancing vs. waiting analysis
- Break cost calculations
- 4-strategy comparison
- Interactive optimization tool
- 30-year benefit projections

**Input Fields Required**: 9 new mortgage-related fields
**Output**: Multi-strategy comparison showing energy + mortgage combined benefits
**Result**: Shows complete financial picture - energy improvements can improve mortgage terms worth €50,000-€100,000+ over loan lifetime!


---

## PART 6: TWO-STAGE SYSTEM - INITIAL ASSESSMENT + CONTINUOUS OPTIMIZATION

### Overview: From One-Time Calculator to Continuous Energy Guardian

The system operates in **two distinct stages**:

**STAGE 1: Initial High-Level Assessment** (Day 1)
- Statistical benchmarking against similar homes
- Thermal efficiency diagnosis
- Priority recommendations
- Implementation roadmap

**STAGE 2: Continuous Agent Monitoring** (Ongoing)
- Real-time energy leak detection
- Smart home integration
- Occupancy-based optimization
- Automated alerts and actions
- Performance verification

---

## STAGE 1: INITIAL HIGH-LEVEL ASSESSMENT

### Statistical Benchmarking & Thermal Efficiency Diagnosis

#### Required Data for Statistical Analysis:

```
📊 STATISTICAL COMPARISON DATA

Home Characteristics (already collected):
✓ Square meters
✓ Volume (m³)
✓ Home age
✓ Energy label
✓ Current systems (heating, insulation, windows)
✓ Location (postal code)

Energy Usage (already collected):
✓ Annual electric consumption (kWh)
✓ Annual gas consumption (m³)
✓ Monthly patterns (if provided)

Additional Context:
Number of occupants: [___] people
   (Helps normalize energy use per person)
Home occupancy pattern:
   ○ Always home (work from home)
   ○ Daytime empty (9-5 jobs)
   ○ Mixed schedule
   ○ Retired/always someone home
```

---

### Thermal Insulation Assessment (Statistical Method)

#### How the Calculator Determines Insulation Quality:

**Method 1: Energy Intensity Analysis**

```
THERMAL EFFICIENCY CALCULATION

Your home:
Volume: 250 m³
Annual gas: 1,450 m³
Annual electric (heating): 850 kWh

Heating energy per m³ volume:
Gas: (1,450 m³ × 9.77 kWh/m³) / 250 m³ = 56.7 kWh/m³/year
Electric: 850 kWh / 250 m³ = 3.4 kWh/m³/year
Total: 60.1 kWh/m³/year

BENCHMARKING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Heating Intensity  │ Insulation Quality │ Typical Label
───────────────────│────────────────────│──────────────
< 25 kWh/m³/year   │ Excellent          │ A++, A+, A
25-35 kWh/m³/year  │ Very Good          │ A, B
35-50 kWh/m³/year  │ Good               │ B, C
50-70 kWh/m³/year  │ Fair               │ C, D
70-100 kWh/m³/year │ Poor               │ D, E, F
> 100 kWh/m³/year  │ Very Poor          │ F, G

YOUR ASSESSMENT: 60.1 kWh/m³/year
Classification: FAIR (lower end)
Likely actual insulation: Between Poor and Fair
Estimated label: D (possibly E)

⚠️ INDICATION: Below average thermal efficiency
Recommendation: Insulation improvements HIGH PRIORITY
```

---

**Method 2: Degree Day Normalization**

```
CLIMATE-ADJUSTED ANALYSIS

Your location: Amsterdam (Postal code 1012)
Annual heating degree days (HDD): 2,785

Your heating energy: 14,165 kWh
Energy per HDD: 14,165 / 2,785 = 5.09 kWh/HDD

COMPARISON TO SIMILAR HOMES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Amsterdam, 100m², Built 1995:

Percentile  │ kWh/HDD │ Your Position
────────────│─────────│──────────────────────
Top 10%     │ 2.1     │ (Well insulated)
25%         │ 3.2     │
50% (Avg)   │ 4.5     │
75%         │ 6.8     │ ← YOU ARE HERE
Bottom 10%  │ 9.2     │ (Poorly insulated)

YOUR ASSESSMENT:
You use 13% MORE heating energy than the median
You are in the 75th percentile (worse than 75% of homes)

THERMAL EFFICIENCY GRADE: D (Bottom 25%)

TRANSLATION:
Your home loses heat faster than 75% of similar homes.
Primary cause: Insufficient insulation and/or air leakage.

TOP RECOMMENDATIONS:
1. Thermal imaging inspection (identify leaks)
2. Attic insulation upgrade (biggest impact)
3. Air sealing (quick win)
4. Wall insulation assessment
```

---

**Method 3: Heating Load Calculation**

```
THEORETICAL VS ACTUAL HEATING DEMAND

Theoretical calculation:
Volume: 250 m³
Design temp: -5°C outside, 20°C inside
Heat loss coefficient (estimated): 250W/K

Annual heating need (theoretical): 8,950 kWh

Your actual heating use: 14,165 kWh

EFFICIENCY RATIO: 63.2%
(You need 58% MORE than theoretical minimum)

WHAT THIS MEANS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Excellent (>85%):  Minimal heat loss, great insulation
Good (70-85%):     Normal heat loss, adequate insulation
Fair (55-70%):     ← YOU ARE HERE
Poor (40-55%):     Significant heat loss
Very Poor (<40%):  Severe insulation problems

YOUR DIAGNOSIS:
Estimated heat loss breakdown:
• Roof/attic: 35% (1,750 kWh/year lost)
• Walls: 30% (1,500 kWh/year lost)
• Windows: 20% (1,000 kWh/year lost)
• Ventilation: 10% (500 kWh/year lost)
• Floor: 5% (250 kWh/year lost)

PRIORITY ORDER:
1. Attic insulation (35% of losses)
2. Wall insulation (30% of losses)
3. Window upgrade (20% of losses)
```

---

### Initial Assessment Output:

```
🏠 THERMAL EFFICIENCY REPORT

Overall Grade: D (Fair - Bottom 25%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY FINDINGS:

✓ GOOD ASPECTS:
• Below average for homes of your age (1995)
  (Many from that era are worse)
• Heating system efficiency: Good (HR boiler)

⚠️ CONCERNS:
• Heat loss 58% above theoretical minimum
• Using 13% more energy than median similar home
• Estimated €880/year in preventable heat loss

🔍 LIKELY ISSUES (Statistical Analysis):

HIGH PROBABILITY (>80% confidence):
• Insufficient attic insulation
  Evidence: High per-m³ energy use
  Estimated Rc value: 2.0-2.5 (should be 6.0)
  Annual loss: ~€300

MODERATE PROBABILITY (60-80%):
• Wall insulation gaps or absent
  Evidence: Built 1995, cavity wall era
  Many homes from this period: Unfilled cavities
  Annual loss: ~€250

LOWER PROBABILITY (40-60%):
• Air leakage around windows/doors
  Evidence: Higher than expected gas use in mild weather
  Annual loss: ~€180

RECOMMENDATIONS:

IMMEDIATE (High-confidence issues):
1. Professional thermal imaging scan (€250-400)
   → Confirms insulation gaps visually
   → Identifies exact problem areas
   → Guides targeted improvements

2. Attic insulation upgrade (€2,500)
   → Address 35% of heat loss
   → Payback: 8.3 years
   → Quick win, accessible

SHORT-TERM (Likely beneficial):
3. Cavity wall insulation (€3,500)
   → Address 30% of heat loss
   → Payback: 14 years
   → Permanent solution

4. Air sealing (€1,200)
   → Address 10-15% of loss
   → Payback: 6.7 years
   → Easy, fast installation

NEXT STEPS:
[ ] Schedule thermal imaging
[ ] Get insulation quotes
[ ] Proceed to Stage 2: Continuous Monitoring
    (Validates improvements, detects new issues)
```

---

## STAGE 2: CONTINUOUS AGENT MONITORING

### Overview: Your 24/7 Energy Guardian

Once initial improvements are underway (or even before), users can activate **Stage 2: Continuous Agent**, which:

1. **Monitors** real-time energy consumption
2. **Detects** anomalies and energy leaks
3. **Learns** patterns and optimizes automatically
4. **Alerts** users to issues and opportunities
5. **Validates** whether improvements are working

---

### Required Integration & Data Sources:

#### Option A: Smart Meter Connection (Recommended)

```
⚡ SMART METER INTEGRATION

Netherlands P1 Port Connection:
Your smart meter has a P1 port (Dutch standard)

Connection methods:
1. Direct USB reader (€25-50)
   → Plug into home server/Raspberry Pi
   → Reads every 10 seconds
   
2. WiFi P1 reader (€60-100)
   → Wireless connection to smart meter
   → Sends data to cloud/app
   → Brands: HomeWizard, Slimme Meter, YouLess

3. Utility company API
   → Some utilities provide hourly data
   → Examples: Vattenfall, Eneco API access
   → Free, but less granular

Data provided:
✓ Real-time electric usage (W)
✓ Real-time gas usage (L/hour)
✓ Daily/weekly/monthly totals
✓ Tariff periods (high/low if applicable)
✓ Solar production (if installed)

RECOMMENDED: Option 2 (WiFi P1 Reader)
Cost: €80 one-time
Provides: 10-second resolution data
Compatible: All Dutch smart meters (DSMR 5.0)

[Shop for P1 Reader] [Setup Guide] [Skip for now]
```

---

#### Option B: Smart Home Integration (Advanced)

```
🏠 SMART HOME ECOSYSTEM INTEGRATION

Connect your existing smart home:

Supported platforms:
☐ Google Home / Nest
☐ Apple HomeKit
☐ Amazon Alexa
☐ Home Assistant (local)
☐ Homey (Dutch platform)
☐ Tado (smart thermostat)
☐ Philips Hue (lighting)

Data we can access (with your permission):
✓ Thermostat: Temperature, setpoint, heating status
✓ Smart plugs: Device-level consumption
✓ Motion sensors: Occupancy detection
✓ Door/window sensors: Open/closed status
✓ Temperature sensors: Room-by-room temps
✓ Humidity sensors: Moisture levels
✓ Smart lights: Usage patterns (occupancy proxy)

Privacy:
• All data processed locally when possible
• Cloud data encrypted end-to-end
• No sharing with third parties
• User can disconnect anytime

[Connect Smart Home] [Manual sensor setup] [Skip]
```

---

#### Option C: Manual Sensor Installation (Budget Option)

```
📡 RECOMMENDED SENSOR KIT

For complete monitoring without existing smart home:

BASIC KIT (€120):
• 1× WiFi thermostat (€80)
  → Tado, Netatmo, or generic
• 3× Temperature sensors (€15 each)
  → Living room, bedroom, attic
  
STANDARD KIT (€250):
• 1× WiFi thermostat (€80)
• 5× Temp/humidity sensors (€20 each)
  → All main rooms
• 1× Smart plug with power monitoring (€25)
  → For heating/major appliance
• 1× Door/window sensor (€25)
  → Detect when heating while windows open

ADVANCED KIT (€450):
• 1× Smart thermostat with room control (€200)
• 8× Temp/humidity sensors (€20 each)
• 3× Motion sensors (€25 each)
• 5× Smart plugs (€25 each)
• 3× Door/window sensors (€15 each)

RECOMMENDED: Standard Kit
Provides 80% of benefit at reasonable cost

[Order Recommended Kit] [Build Custom] [Skip]
```

---

### Continuous Monitoring Features:

#### Feature 1: Real-Time Energy Leak Detection

```
🚨 ENERGY LEAK DETECTION SYSTEM

How it works:
1. Learns your normal energy patterns (2-4 weeks)
2. Detects anomalies in real-time
3. Correlates with temperature, occupancy, time
4. Alerts you to issues immediately

EXAMPLE ALERTS:

Alert Type: HIGH HEATING USE
Detected: 15:24, January 12, 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Heating spike detected

Current usage: 4.2 kW (heating)
Expected: 1.8 kW for this time/temp
Excess: 133% above normal

Possible causes:
1. Window/door left open (check sensors)
2. Thermostat set too high (current: 22°C, usual: 20°C)
3. Heating system malfunction

Detected pattern:
Started: 14:45 (37 minutes ago)
Location: Living room temp dropped to 18°C then spiked
Likely: Window opened, heating compensating

RECOMMENDATION:
Close living room window
Estimated cost if continues: €6.80/day = €204/month

[Close window reminder sent to phone]
[Mark as false alarm]
[Investigate further]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Alert Type: STANDBY POWER DRAIN
Detected: 02:15, January 13, 2025
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Unnecessary power consumption

Nighttime baseline: 185W
Expected: 80-100W (refrigerator, router, etc.)
Excess: 85-105W

Analysis:
• Living room: 45W constant
• Kitchen: 35W constant
• Office: 25W constant

Likely culprits:
1. TV/entertainment system on standby (35-50W)
2. Computer left on in office (20-30W)
3. Kitchen appliances on standby (10-20W)

Annual cost of excess standby: €165/year

RECOMMENDATION:
• Install smart plugs on entertainment center
• Enable auto-off for computer after 30 min idle
• Consider master power strip for kitchen

Potential savings: €165/year for €75 investment
Payback: 5.5 months

[Order smart plugs] [Remind me tomorrow]
[Ignore this alert type]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

#### Feature 2: Occupancy-Based Automation

```
🏡 SMART OCCUPANCY CONTROL

Setup:
1. Install motion/door sensors (or use phone location)
2. Set temperature preferences per room
3. Define "away" mode rules
4. Agent learns and optimizes

AUTOMATIC ACTIONS:

Nobody Home Detection:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Trigger: No motion for 30 minutes + phones left geofence
Time: 09:15

Automatic actions taken:
✓ Thermostat: 20°C → 17°C (savings mode)
✓ Living room lights: Off
✓ Office heater: Off
✓ Bedroom radiators: Reduced

Estimated savings: €2.80/day when away 8+ hours
Monthly impact: ~€60/month in winter

[Adjust away temperature] [Change sensitivity]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Room-Level Optimization:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Guest bedroom (not used last 5 days):

Current: Heating to 18°C (frost protection)
Learned pattern: Used only weekends
Agent recommendation: 
• Weekdays: 15°C (minimal)
• Friday 6pm: Pre-heat to 20°C
• Monday morning: Back to 15°C

Savings: €45/month in winter

AUTO-APPLIED (can disable):
✓ Guest bedroom schedule updated
✓ Pre-heating reminder set for guests

[View all room schedules] [Override]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Predictive Pre-Heating:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Agent learned your schedule:
Monday-Friday: Arrive home 18:00-18:30

Smart pre-heat strategy:
• Start heating: 17:15 (45 min before)
• Ramp from 17°C to 20°C gradually
• Home comfortable when you arrive
• Uses off-peak rate if applicable

Compared to all-day heating:
Savings: €3.20/day × 5 days = €16/week

[Adjust arrival time] [Weekend schedule]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

#### Feature 3: Temperature vs. Energy Analysis

```
📊 PERFORMANCE CORRELATION ANALYSIS

Tracks: Outside temp vs. energy use over time
Purpose: Validate improvements, detect degradation

BASELINE ESTABLISHMENT (Week 1-4):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Learning your home's heat loss rate...

Data collected:
• Outside temp: Weather API (per hour)
• Inside temp: Your sensors (per 10 min)
• Gas usage: Smart meter (per 10 sec)
• Heating cycles: Thermostat data

Analysis:
Outside Temp │ Avg Gas Use │ Heating Hours
─────────────│─────────────│──────────────
-2°C to 0°C  │ 6.8 m³/day  │ 18 hrs/day
0°C to 5°C   │ 5.2 m³/day  │ 14 hrs/day
5°C to 10°C  │ 3.4 m³/day  │ 9 hrs/day
10°C to 15°C │ 1.8 m³/day  │ 4 hrs/day

Heat loss coefficient calculated: 385 W/K
(Your home loses 385W of heat per degree difference)

BASELINE ESTABLISHED ✓
Now monitoring for changes...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AFTER ATTIC INSULATION (Month 3):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Improvement installed: February 15, 2025
Monitoring impact...

Comparison (same temperatures):
Before │ After  │ Change
───────│────────│─────────────────
6.8 m³ │ 5.4 m³ │ -20.6% (0°C)
5.2 m³ │ 4.2 m³ │ -19.2% (5°C)
3.4 m³ │ 2.8 m³ │ -17.6% (10°C)

New heat loss coefficient: 310 W/K
Improvement: 19.5% reduction ✓

VALIDATION:
Expected savings: 15-25% (attic insulation)
Actual measured: 19.5%
Status: PERFORMING AS EXPECTED ✓

Annual savings (based on measured):
Gas saved: 284 m³/year
Cost savings: €426/year
ROI confirmed: 5.9 year payback

[View detailed chart] [Download report]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEGRADATION DETECTION (Month 18):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Performance anomaly detected

Recent pattern (last 2 weeks):
Heat loss coefficient: 310 W/K → 340 W/K
Increase: 9.7% (unexpected)

Same outside temps now using MORE gas than Month 12

Possible causes:
1. Insulation settlement/compression
2. New air leak (window seal, door gap)
3. Ventilation system issue
4. Roof damage affecting insulation

RECOMMENDATION:
Schedule inspection to identify cause
Potential annual cost: €85 in excess heating

[Schedule inspection] [Monitor 2 more weeks]
[View historical chart]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

#### Feature 4: Humidity & Moisture Monitoring

```
💧 HUMIDITY MONITORING & ALERTS

Why it matters:
• High humidity = mold risk
• Low humidity = discomfort, health issues
• Humidity affects heating efficiency

NORMAL MONITORING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Room          │ Temp  │ Humidity │ Status
──────────────│───────│──────────│─────────
Living room   │ 20.5°C│ 52%      │ ✓ Ideal
Kitchen       │ 21.0°C│ 58%      │ ✓ Good
Bathroom      │ 22.0°C│ 68%      │ ⚠️ High
Bedroom       │ 19.5°C│ 48%      │ ✓ Good
Attic         │ 12.0°C│ 75%      │ ⚠️ Monitor

Recommendations:
• Bathroom: Vent fan after shower (auto-reminder)
• Attic: Check for roof leaks (high humidity)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ALERT EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ MOLD RISK DETECTED

Location: Bedroom (north-facing)
Time: 07:45, January 20, 2025

Conditions:
• Temperature: 16.5°C (too cold)
• Humidity: 72% (too high)
• Duration: 6+ hours at these levels

Mold risk: HIGH (48-hour exposure at these levels)

Immediate actions:
1. Increase bedroom heating to 18°C minimum
2. Open window for 10 minutes (ventilate)
3. Check for condensation on windows

Long-term fixes:
• Better insulation (prevent cold surfaces)
• Improved ventilation (WTW system)
• Thermal bridge repair (common in corners)

[Take action now] [Snooze 1 hour] [Learn more]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

#### Feature 5: Smart Recommendations Engine

```
💡 WEEKLY OPTIMIZATION REPORT

Delivered: Every Monday morning
Based on: Previous week's data + weather forecast

EXAMPLE REPORT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Your Energy Week in Review
Week of January 13-19, 2025

PERFORMANCE:
✓ Energy use: 15% below similar homes
✓ Average temp maintained: 20.1°C
⚠️ 2 anomalies detected (both resolved)

INSIGHTS:

1. Thursday Evening Peak
   Detected: 18:00-22:00, all lights + heating high
   Cost: €4.20 extra
   Suggestion: Use smart scene "Evening" 
   → Dims lights, reduces heating when cooking
   Potential savings: €8/week

2. Weekend Oversleeping
   Bedroom heated to 20°C but empty until 10am
   Cost: €3.60 wasted
   Suggestion: Weekend heating delay
   Potential savings: €15/month

3. Unused Office Heating
   Office heated Mon-Fri despite WFH Tue/Thu
   Cost: €5.40/week wasted
   Suggestion: Smart schedule based on calendar
   Potential savings: €23/month

WEATHER FORECAST OPTIMIZATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Next 7 days: Warmer trend (12°C → 15°C by Friday)

Recommendations:
Monday-Wednesday: Current settings optimal
Thursday: Reduce heating 1°C (outdoor 14°C)
Friday-Sunday: Further reduce 1°C (outdoor 15°C)
Estimated savings this week: €8.50

[Auto-apply schedule] [Review changes]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONTHLY CHALLENGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Goal: Reduce energy 10% vs. last January

Progress: 8.2% reduction so far ✓
On track to save: €28 this month

Next steps to hit 10%:
• Shorten shower times 1 minute (saves 3%)
• Lower nighttime temp to 17°C (saves 2%)

[Accept challenge] [View leaderboard]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## INTEGRATION: STAGE 1 + STAGE 2 WORKFLOW

```
COMPLETE USER JOURNEY:

DAY 1: Initial Assessment
├─ User fills calculator with home data
├─ Statistical analysis: "Thermal efficiency Grade D"
├─ High-level recommendations generated
└─ Suggested: Install sensors for Stage 2

WEEK 1-4: Baseline Learning
├─ User installs P1 reader + temp sensors
├─ Agent learns normal patterns
├─ No actions yet, just observation
└─ Baseline established

MONTH 2: Start Improvements
├─ User installs attic insulation (based on Stage 1)
├─ Agent monitors before/after performance
├─ Validates 19.5% improvement (expected 15-25%)
└─ ROI confirmed ✓

MONTH 3-6: Optimization Phase
├─ Agent detects energy leaks in real-time
├─ Suggests schedule optimizations
├─ Occupancy-based automation enabled
├─ Weekly reports show continuous improvement
└─ Additional 12% savings from optimization

MONTH 7+: Maintenance & Alerts
├─ Agent monitors for degradation
├─ Alerts to unusual patterns
├─ Seasonal optimization (summer/winter)
├─ Validates all improvements still working
└─ Suggests new opportunities

YEAR 2: Annual Review
├─ Complete performance report
├─ Comparison: Predicted vs. actual savings
├─ Identified: €1,340 saved (vs €1,150 predicted)
├─ Agent suggests next improvements
└─ Plan Year 2 upgrades
```

---

## REQUIRED INFRASTRUCTURE & PERMISSIONS

### Data Collection & Privacy:

```
🔒 DATA COLLECTION CONSENT

The continuous monitoring agent requires:

TIER 1: Basic Monitoring (Minimum)
☐ Smart meter data (10-second intervals)
   → Electric & gas consumption
   → Used for: Leak detection, baseline

TIER 2: Environmental Monitoring
☐ Temperature sensors (room-level)
☐ Humidity sensors
   → Used for: Comfort, mold prevention

TIER 3: Occupancy Detection
☐ Motion sensors OR
☐ Phone location (geofence) OR
☐ Smart home integration
   → Used for: Automated scheduling

TIER 4: Smart Home Control
☐ Thermostat control
☐ Smart plug control
☐ Lighting control (optional)
   → Used for: Automated optimization

Privacy Guarantees:
✓ All data encrypted in transit and at rest
✓ No data sold or shared with third parties
✓ Local processing when possible
✓ User can view/delete all data anytime
✓ Granular control over what's collected
✓ Option to export all your data

[Accept All Tiers] [Customize] [Decline Monitoring]
```

---

## COST OF STAGE 2 MONITORING

```
💰 CONTINUOUS MONITORING COST

OPTION A: Basic (Smart Meter Only)
Hardware: €80 (WiFi P1 reader, one-time)
Software: Free (included in initial plan)
Capabilities: Energy tracking, leak detection
Limitations: No occupancy automation

OPTION B: Standard (+ Temperature Sensors)
Hardware: €250 (P1 + 5 sensors, one-time)
Software: Free
Capabilities: + Room optimization, comfort alerts
Limitations: Manual schedule adjustments

OPTION C: Advanced (Full Smart Home)
Hardware: €450 (Full sensor kit, one-time)
Software: €4.99/month (cloud processing, advanced AI)
Capabilities: Full automation, predictive, calendar sync
Benefits: Hands-free optimization

OPTION D: Premium (+ Professional Support)
Hardware: €450 (one-time)
Software: €9.99/month
Capabilities: + Human advisor access, priority support
Bonus: Annual thermal imaging inspection included

RECOMMENDATION: Option B (Standard)
Best value for most users
Payback: 3-6 months from detected savings

Typical savings from monitoring:
Basic: €180/year (leak detection alone)
Standard: €420/year (+ automation)
Advanced: €650/year (full optimization)
Premium: €820/year (+ expert guidance)

[Start with Basic] [Choose Standard] [Go Advanced]
```

---

**Section Added**: Two-Stage System Framework
**Stage 1 Features**:
- Statistical benchmarking (percentile ranking)
- Thermal efficiency diagnosis (3 methods)
- Heat loss coefficient calculation
- Degree day normalization
- Initial assessment with confidence levels

**Stage 2 Features**:
- Real-time energy leak detection
- Occupancy-based automation
- Temperature vs. energy correlation
- Performance validation (before/after)
- Humidity & mold monitoring
- Weekly optimization reports
- Degradation alerts
- Weather-based scheduling

**Integration**: Smart meter (P1 port), smart home platforms, manual sensors
**Privacy**: Tiered consent, local processing, full user control
**Cost**: €80-€450 hardware + €0-€10/month software
**ROI**: 3-6 month payback from detected savings

**Result**: Transforms one-time calculator into continuous energy guardian that detects issues, validates improvements, and optimizes automatically!


---

## PART 6: TWO-STAGE INTELLIGENCE SYSTEM

### Overview: From Static Analysis to Continuous Optimization

The calculator operates in **two distinct stages**:

**STAGE 1: Initial High-Level Recommendations** (Immediate)
- Statistical thermal analysis
- Benchmark comparison
- Priority action plan
- One-time calculation based on entered data

**STAGE 2: Continuous Optimization Agent** (Ongoing via WhatsApp)
- Real-time energy monitoring
- Automated leak detection
- Behavior optimization
- Smart home integration
- Effect measurement
- Adaptive recommendations

---

## STAGE 1: HIGH-LEVEL RECOMMENDATIONS (IMMEDIATE)

### Statistical Thermal Analysis

Based on home data entered, calculator performs thermal performance analysis using statistical models:

---

### 1A. Thermal Insulation Assessment

#### Required Data Points:
```
FROM USER INPUT:
• Square meters: 120 m²
• Volume: 300 m³
• Home age: 28 years
• Energy label: D
• Current insulation: Fair (Rc 3.5)
• Window type: Double glazing
• Heating system: Gas boiler, 15 years
• Annual gas usage: 1,800 m³
• Annual electric usage: 3,600 kWh
• Floor heating: Living room only
• Ventilation: Natural (no WTW)
```

#### Statistical Benchmarking:

```
📊 THERMAL PERFORMANCE ANALYSIS

Comparing your home to statistical database:
(125,000+ Dutch homes in similar category)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOUR HOME THERMAL PROFILE:

Heat Loss Coefficient (W/K): 385 W/K
Expected for your size: 280-320 W/K
Your status: ⚠️ 25% ABOVE AVERAGE

Breakdown by component:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Walls (cavity, Rc 3.5):
Your heat loss: 145 W/K
Expected: 95-110 W/K
Status: ⚠️ POOR (32% above average)
Diagnosis: Likely partial/degraded insulation
Priority: HIGH - Wall insulation upgrade needed

Roof/Attic (Rc 3.5):
Your heat loss: 85 W/K  
Expected: 50-65 W/K
Status: ⚠️ FAIR (31% above average)
Diagnosis: Insulation settled/compressed over time
Priority: MEDIUM - Attic top-up recommended

Windows (double glazing):
Your heat loss: 95 W/K
Expected: 80-95 W/K
Status: ✓ ACCEPTABLE
Diagnosis: Age-appropriate performance
Priority: LOW - Upgrade later in plan

Floor (uninsulated, typical 1990s):
Your heat loss: 40 W/K
Expected: 30-40 W/K
Status: ✓ ACCEPTABLE
Diagnosis: Normal for age
Priority: LOW

Ventilation (natural, no heat recovery):
Your heat loss: 120 W/K
Expected: 45-60 W/K (with WTW)
Status: ⚠️ VERY POOR (100% higher!)
Diagnosis: No heat recovery system
Priority: HIGH - WTW installation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATISTICAL CONFIDENCE ANALYSIS:

Data quality: 87% (Good)
├─ Bill data: Complete ✓
├─ System details: Partial (missing WTW specs)
└─ Floor plan: Not provided

Accuracy range: ±12%
Recommendation: Upload floor plan for ±5% accuracy

Similar homes analysis:
Homes like yours (120m², 1995-2000, Label D):
  - Average gas: 1,650 m³/year
  - Your usage: 1,800 m³/year (+9%)
  - Top 25% use: 1,450 m³/year
  
Your potential: Reduce to 1,100 m³/year (39% savings)
with full thermal optimization

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THERMAL WEAK POINTS DETECTED:

🔴 CRITICAL (Immediate attention):
1. Ventilation heat loss (€480/year wasted)
2. Wall insulation degraded (€380/year wasted)

🟡 IMPORTANT (Plan for this year):
3. Attic insulation settling (€240/year wasted)

🟢 MONITOR (Future consideration):
4. Window efficiency (minor loss)
5. Floor insulation (small impact)

TOTAL ADDRESSABLE WASTE: €1,100/year

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPARISON TO IDEAL:

Your home: 385 W/K heat loss
Best practice (Label A): 180 W/K
Realistic target (Label B): 240 W/K

Gap to close: 145 W/K (38% improvement needed)

Recommended path to Label B:
✓ Wall insulation: -70 W/K
✓ WTW ventilation: -75 W/K
✓ Attic top-up: -20 W/K
= Target achieved: 220 W/K (Label B range)

[View Detailed Thermal Map] [Export Analysis]
```

---

### 1B. Statistical Anomaly Detection

```
🔍 ANOMALY DETECTION RESULTS

Comparing your usage patterns to statistical norms:

ANOMALY 1: High Gas Usage in Summer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your summer gas (Jun-Aug): 180 m³
Expected: 90-120 m³ (hot water only)
Excess: 60-90 m³ (+50-75%)

Likely causes (ranked by probability):
1. 68% - Poorly insulated hot water tank/pipes
2. 22% - Boiler pilot light inefficiency  
3. 10% - Hot water usage higher than average

Recommended actions:
✓ Insulate hot water tank (€80, saves €65/year)
✓ Insulate hot water pipes (€120, saves €45/year)
✓ Check boiler efficiency (free, may save 10%)

ANOMALY 2: Weekend Electric Spikes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your weekend usage: 35% higher than weekdays
Expected: 15-20% higher
Excess: +15-20 percentage points

Likely causes:
1. Home all weekend (normal behavior)
2. Possible: Old appliances inefficient
3. Possible: Electric heating supplement

Recommended actions:
⚠️ Stage 2 monitoring recommended
   → Identify specific appliances
   → Track usage patterns
   → Optimize timing

ANOMALY 3: High Standby Consumption
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Estimated baseload: 180W continuous
Expected: 80-120W
Excess: 60-100W

Annual waste: 525-875 kWh (€158-€263/year)

Likely culprits:
1. Always-on devices (TV, router, etc.)
2. Inefficient appliances on standby
3. Phantom loads (chargers, etc.)

Recommended actions:
✓ Smart plugs to measure (€60)
✓ Stage 2 monitoring for identification
✓ Behavior changes (€0, saves €100-€200/year)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATISTICAL CONFIDENCE:
Anomalies detected: 3 significant
Data certainty: 78% (monthly data incomplete)
Recommendation: Enable Stage 2 for precise diagnosis

[Enable Continuous Monitoring] [View All Anomalies]
```

---

### 1C. Thermal Imaging Simulation (Statistical)

```
🌡️ STATISTICAL THERMAL MAP

Based on home characteristics, we estimate heat loss:
(Upload floor plan for room-by-room precision)

Estimated Heat Loss Distribution:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

     [Roof/Attic: 85 W/K]  22% of total loss
            ↓ ↓ ↓
    ┌─────────────────────────┐
    │ Living Room  │ Bedroom1│
    │ 🌡️ 🟡       │ 🌡️ 🔴   │  [North Wall: 
    │              │          │   145 W/K]
    ├──────────────┼──────────┤   38% loss
    │ Kitchen      │ Bedroom2│
    │ 🌡️ 🟢       │ 🌡️ 🟡   │
    └─────────────────────────┘
            ↓ ↓ ↓
      [Floor: 40 W/K] 10% of total

🔴 RED (Critical): North-facing bedrooms
   - No floor heating
   - Single exterior wall
   - Original 1995 insulation
   - Est. loss: 145 W/K (38% of total)
   
🟡 YELLOW (Moderate): Living room, Bedroom 2
   - Some floor heating (living room)
   - Mixed exposure
   - Est. loss: 125 W/K (32%)

🟢 GREEN (Good): Kitchen
   - Interior location
   - Appliance heat gain
   - Est. loss: 35 W/K (9%)

⚪ VENTILATION (Invisible but major):
   - No heat recovery
   - Est. loss: 120 W/K (31%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TARGETED RECOMMENDATIONS:

Priority 1: North bedrooms
Action: Wall insulation (exterior or cavity fill)
Impact: -70 W/K (-€380/year)

Priority 2: Ventilation
Action: WTW system installation
Impact: -75 W/K (-€480/year)

Priority 3: Roof
Action: Attic insulation top-up
Impact: -20 W/K (-€240/year)

[Upload Floor Plan for Precise Analysis]
[Enable Smart Home Monitoring (Stage 2)]
```

---

### 1D. High-Level Recommendation Summary

```
📋 STAGE 1: INITIAL RECOMMENDATIONS

Based on statistical analysis of your home:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THERMAL PERFORMANCE: ⚠️ BELOW AVERAGE
Your heat loss: 25% above similar homes
Improvement potential: 38% reduction possible

TOP 3 PRIORITIES:

1️⃣ VENTILATION HEAT RECOVERY (WTW)
   Current loss: 120 W/K (31% of total)
   Investment: €3,500-€5,000
   Savings: €480/year
   Payback: 7.3-10.4 years
   Why first: Largest single loss source
   
2️⃣ WALL INSULATION
   Current loss: 145 W/K (38% of total)
   Investment: €4,000-€6,000
   Savings: €380/year
   Payback: 10.5-15.8 years
   Why second: Enables heat pump later
   
3️⃣ ATTIC INSULATION TOP-UP
   Current loss: 85 W/K (22% of total)
   Investment: €1,500-€2,500
   Savings: €240/year
   Payback: 6.3-10.4 years
   Why third: Quick win, DIY possible

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STATISTICAL CONFIDENCE: 78%

To improve accuracy to 95%:
✓ Upload floor plan → +12% accuracy
✓ Enable Stage 2 monitoring → +5% accuracy
✓ Smart home sensors → Real-time precision

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEXT STEPS:

Option A: Proceed with recommendations
[View Detailed Plan] [Get Contractor Quotes]

Option B: Enable continuous monitoring first
[Activate Stage 2 Agent] [Get Smart Home Kit]

Option C: Get more precise analysis
[Upload Floor Plan] [Schedule Thermal Scan]

Most users choose: Option B (monitoring first)
Why: Confirms statistical findings with real data
      Identifies hidden issues before investing
      Costs €0-€200 vs €9,000+ in improvements
```

---

## STAGE 2: CONTINUOUS OPTIMIZATION AGENT

### Overview: Real-Time Intelligent Monitoring

After initial recommendations, users can activate the **Continuous Optimization Agent** via WhatsApp for ongoing monitoring and guidance.

---

### 2A. Real-Time Energy Monitoring Setup

#### Required: Connect Data Sources

```
📊 STAGE 2 SETUP: CONNECT YOUR DATA

To enable continuous monitoring, connect:

OPTION 1: Smart Meter (P1 Port) ✓ RECOMMENDED
Connect via:
├─ WiFi P1 adapter (€25-€60)
├─ HomeWizard P1 meter (€45)
├─ Slimmelezer (€20, DIY)
└─ Direct API (some energy companies)

Provides:
✓ Real-time kWh/gas usage (10-second intervals)
✓ Usage graphs and patterns
✓ Cost tracking
✓ Export to WhatsApp bot

Setup time: 15 minutes
Cost: €20-€60 one-time

[Buy Recommended P1 Adapter]
[DIY Installation Guide]

OPTION 2: Manual Entry (Fallback)
Enter meter readings:
○ Daily (best accuracy)
○ Weekly (good accuracy)  
○ Monthly (basic tracking)

Provides:
✓ Trend analysis
✓ Anomaly detection
✓ Basic optimization
⚠️ No real-time leak detection

Cost: Free
Effort: 2 minutes per entry

[Set Up Manual Entry Schedule]

OPTION 3: Smart Home Integration ⭐ BEST
Connect existing smart home:
├─ Homey Pro
├─ Home Assistant
├─ Google Home
├─ Apple HomeKit
├─ Samsung SmartThings
└─ Philips Hue Bridge

Provides:
✓ Everything from Option 1
✓ Temperature/humidity sensors
✓ Occupancy detection
✓ Appliance-level monitoring
✓ Automated control
✓ Room-by-room optimization

Setup time: 30-60 minutes
Cost: €0 (if existing) or €150-€400 (new system)

[Connect Smart Home] [Buy Starter Kit]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDED PATH FOR YOUR HOME:

Based on your situation (Label D, high heat loss):

Phase 1: Smart Meter P1 (€45)
→ Immediate: Energy pattern tracking
→ Week 1: Identify waste sources

Phase 2: Add Temperature Sensors (€90)
→ 3 sensors: Living room, bedroom, outside
→ Week 2: Thermal monitoring active

Phase 3: Smart Thermostat (€180)
→ Automated heating optimization
→ Week 3: Savings start automatically

Total investment: €315
Expected savings: €250-€400/year
Payback: 9-15 months

Then: Make informed improvement decisions
Based on real data, not estimates

[Start with Phase 1] [Get Complete Kit]
```

---

### 2B. Automated Energy Leak Detection

Once monitoring is active, the WhatsApp bot continuously analyzes data:

```
🔍 CONTINUOUS LEAK DETECTION

The bot monitors your home 24/7 for anomalies:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEAK TYPE 1: Thermal Leaks
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detection method:
→ Compares inside vs outside temperature
→ Measures heating cycle frequency
→ Calculates thermal retention time

Example alert:
[WhatsApp notification - 3:42 AM]

Bot: 🚨 Thermal leak detected!

Location: North bedroom
Issue: Temperature drop 2.3°C/hour
Expected: 0.8°C/hour
Excess loss: 288% faster than normal

Outdoor temp: 2°C
Indoor start: 19°C
Indoor now (6 hours): 5.2°C

Likely causes:
1. 78% - Window left open/ajar
2. 15% - Heating valve closed/broken
3. 7% - Severe insulation failure

Wasted energy: 28 kWh (€12 lost)

Actions:
[Check window] [View temperature graph] 
[I fixed it] [False alarm]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEAK TYPE 2: Appliance Waste Detection
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detection method:
→ Monitors baseload consumption
→ Identifies unusual patterns
→ Learns normal vs abnormal

Example alert:
[WhatsApp notification - 11:23 AM]

Bot: ⚠️ Abnormal power consumption

Event: Sudden 850W load for 3+ hours
Time: Started 8:15 AM (3h 8m ago)
Total wasted so far: 2.7 kWh

Pattern: Unusual for weekday morning
Your typical 8-11 AM: 280W average
Today: 1,130W average

Possible causes:
1. Appliance left on (iron, space heater?)
2. Appliance malfunction
3. New device running

Cost so far: €0.81
Daily cost if continues: €6.12

Actions:
[What's running?] [I know about it]
[Help me find it] [Ignore]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEAK TYPE 3: Heating Inefficiency
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detection method:
→ Correlates heating runtime vs temp gain
→ Compares to baseline efficiency
→ Adjusts for outdoor temperature

Example alert:
[WhatsApp notification - 7:15 PM]

Bot: 📉 Heating efficiency dropped

Observation period: Last 7 days
Your heating efficiency: -23% vs baseline

Details:
To heat home 1°C now takes: 42 minutes
Two weeks ago: 34 minutes
Expected (for weather): 36 minutes

Extra runtime: 6 minutes per degree
Daily extra: ~45 minutes
Weekly waste: 18 kWh (€27/week)

Likely causes:
1. 45% - Radiator valve stuck/clogged
2. 30% - Boiler efficiency degraded
3. 15% - New draft/leak appeared
4. 10% - Thermostat placement issue

Actions:
[Check radiators] [Book boiler service]
[Thermal scan recommended] [Monitor more]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEAK TYPE 4: Vampire Power (Standby)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detection method:
→ Monitors consumption 2-5 AM (sleep hours)
→ Identifies always-on devices
→ Calculates annual waste

Example alert:
[WhatsApp notification - Weekly summary]

Bot: 💡 Standby power analysis

Your night baseload (2-5 AM average):
Current: 187W continuous
Recommended: <100W
Excess: 87W unnecessary

Annual waste: 762 kWh (€229/year)

Likely culprits (ranked):
1. 🔴 65W - Unknown device (new?)
2. 🟡 28W - Entertainment system
3. 🟡 22W - Network equipment  
4. 🟢 18W - Refrigerator (normal)
5. 🟢 15W - Heating pump (normal)

New device detected:
Since Feb 1: Unknown 65W load appeared
Suspect: Recent purchase?

Actions:
[Help identify] [Install smart plugs]
[I'll check manually] [Weekly report]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEAK TYPE 5: Hot Water Waste
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Detection method:
→ Correlates gas usage when heating off
→ Detects continuous low-level consumption
→ Identifies tank heat loss

Example alert:
[WhatsApp notification - 2:34 PM]

Bot: 🚿 Hot water system inefficiency

Detected: Continuous gas consumption
Rate: 0.15 m³/hour (minimal but constant)
Duration: 24/7 for past 14 days
Total waste: 50 m³/month (€75/month!)

Diagnosis: Hot water tank heat loss

Your tank loses heat at: 2.1 kW
Expected: 0.5-0.8 kW
Excess loss: 163-320%

Causes (ranked):
1. 70% - Uninsulated or poorly insulated tank
2. 20% - Uninsulated pipes
3. 10% - Tank thermostat set too high

Solutions:
Quick (DIY): Insulation jacket (€45)
Better: Pipe insulation (€120 total)
Best: Heat pump water heater (€2,000)

Expected savings:
Insulation: €55-€65/month
Payback: <2 months

[Buy insulation kit] [DIY guide]
[Get pro quote] [Monitor more]
```

---

### 2C. Smart Home Integration & Occupancy-Based Control

For advanced users with smart home systems:

```
🏠 SMART HOME OPTIMIZATION

When you connect a compatible smart home system,
the bot enables advanced features:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEATURE 1: Occupancy-Based Heating
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Setup:
✓ Motion sensors in each room
✓ Door/window sensors
✓ Smart radiator valves (TRVs)
✓ Or: smart thermostat with geofencing

How it works:
1. Detects who is where in real-time
2. Adjusts heating per room
3. Reduces temperature in empty rooms
4. Pre-heats before arrival

Example automation:
[WhatsApp setup wizard]

Bot: 🎯 Let's set up occupancy heating

For each room, I need to know:
• Normal occupied temperature
• Reduced temperature when empty
• Pre-heat time before expected return

Living Room:
Occupied temp: [20]°C
Away temp: [16]°C (save 15% energy)
Pre-heat: [30] minutes before arrival
Sensors: Motion sensor, window sensor

Bedroom (main):
Occupied: [18]°C (night), [16]°C (day)
Away: [15]°C
Pre-heat: [15] minutes
Sensors: Motion, bed sensor

[Continue for all rooms]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bot learns and adapts:

Week 1: Following schedule you set
Week 2-4: Learning your patterns
Week 5+: Predictive adjustment

Example learned behavior:
"User typically arrives home 18:15-18:45
 on weekdays. Pre-heat starting 17:45.
 On Wednesdays, often 30 min later.
 Adjusting Wednesday pre-heat to 18:15."

Savings: 18-28% on heating costs
Typical: €280-€420/year

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEATURE 2: Multi-Zone Climate Optimization
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sensors required:
✓ Temperature sensor per room (€15-€25 each)
✓ Humidity sensor per room (included or +€10)
✓ Outside temperature sensor

Bot maintains optimal climate per room:

Living Room:
Target: 20°C, 45-55% humidity
Current: 19.8°C, 52% ✓ Optimal

Bedroom (north):
Target: 18°C night, 50% humidity
Current: 16.2°C, 38% ⚠️ Too dry

Bot action:
[Notification 9:42 PM]

Bot: 🌡️ Bedroom conditions sub-optimal

Temp: 16.2°C (target 18°C)
Humidity: 38% (target 50%)

Actions taken automatically:
✓ Increased radiator valve 15%
✓ Suggested: Run humidifier 20 min

Outside: -2°C, will reach 18°C in 23 min

Health note: Low humidity at night can
affect sleep quality and respiratory health.

[View climate history] [Adjust targets]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEATURE 3: Automated Ventilation Control
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If you have mechanical ventilation (WTW):

Bot monitors:
✓ CO₂ levels (if sensors available)
✓ Humidity levels
✓ Occupancy
✓ Outdoor air quality (from API)

Auto-adjusts ventilation:

Example:
[Notification 19:15]

Bot: 🌬️ Air quality optimization

Kitchen CO₂: 1,250 ppm (elevated)
Cause: Cooking detected
Action: Ventilation boost +40% for 20 min

Bedroom humidity: 68% (too high)
Cause: Shower 15 min ago
Action: Bathroom exhaust boost 15 min

Living room: 4 people detected
Normal: 2 people
Action: Slight ventilation increase

Outside air quality: Good (AQI 35)
Safe to increase fresh air intake

[View air quality dashboard]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FEATURE 4: Window Open Detection & Response
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sensors: Window/door contact sensors

Automation:
When window opens during heating season:
→ Immediately reduce radiator in that room
→ Notify user if window stays open >10 min
→ Track ventilation vs energy waste

Example:
[Notification 14:23]

Bot: 🪟 Window open in bedroom

Detected: Bedroom window opened 14:21
Action: Radiator reduced to 12°C (from 18°C)
Savings: Preventing waste during airing

Reminder in 10 minutes if still open.

[14:33 - Window still open]

Bot: Window open 12 minutes

Outside: 4°C
Inside: 17.1°C (dropping 0.9°C per 10 min)
Energy waste so far: 1.2 kWh (€0.36)

Recommendation: Close now to preserve heat
Or: I'll auto-heat when you close

[I closed it] [Keep me updated]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SMART HOME INVESTMENT TIERS:

TIER 1: Basic Monitoring (€60-€150)
• P1 smart meter reader (€45)
• 2-3 temperature sensors (€50-€75)
• Manual control via phone

Savings: €150-€250/year
Payback: 3-7 months

TIER 2: Automated Control (€300-€500)
• Everything in Tier 1
• Smart thermostat (€180-€250)
• 4-6 temp/humidity sensors (€120-€180)
• Window sensors (€60-€100)
• Basic automation

Savings: €350-€550/year
Payback: 7-14 months

TIER 3: Full Optimization (€800-€1,500)
• Everything in Tier 2
• Smart radiator valves (€200-€400)
• Occupancy sensors (€150-€300)
• Air quality sensors (€100-€200)
• Advanced automation hub (€150-€300)

Savings: €600-€900/year
Payback: 13-25 months

[Get Tier 1 Kit] [Full Comparison]
```

---

### 2D. Effect Measurement & Validation

```
📈 MEASURING IMPROVEMENT EFFECTIVENESS

After each action/improvement, bot tracks impact:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MEASUREMENT PROTOCOL:

Baseline Period (Before):
Duration: 2-4 weeks before improvement
Data collected:
• Daily energy usage
• Degree days (heating adjusted for weather)
• Room temperatures
• Usage patterns

Improvement Event:
Date: [Marked in system]
Type: [Insulation/Equipment/Behavior/etc.]
Expected impact: [Calculated estimate]

Measurement Period (After):
Duration: 4-8 weeks after improvement
Same data collection
Weather-adjusted comparison

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXAMPLE: Wall Insulation Impact

[Before - 4 weeks baseline]
Average daily gas: 8.2 m³/day
Degree days: 385
Normalized usage: 7.8 m³/day (weather-adjusted)

[Improvement completed: Wall insulation - Feb 14]

[After - Week 1]

Bot: 📊 Week 1 results: Wall insulation

Early indicators (7 days):
Gas usage: 6.9 m³/day (avg)
Degree days: 392 (similar weather)
Normalized: 6.6 m³/day

IMPACT: -15.4% vs baseline ✓

Expected: -12 to -18%
Result: Within expected range

Indoor temp stability:
Before: ±2.1°C variation
After: ±1.3°C variation (38% more stable)

Confidence: 72% (need more days)

[View detailed graphs] [Compare to prediction]

[After - Week 4]

Bot: 📊 Month 1 results: Wall insulation

Measurement complete (28 days):
Gas usage: 6.4 m³/day (avg)
Weather-adjusted: 6.2 m³/day

IMPACT: -20.5% vs baseline ✅

Expected: -12 to -18%
Result: BETTER than expected (+2.5%)

Possible reasons for better performance:
1. Insulation quality exceeded spec
2. Sealed more air leaks during install
3. Previous insulation worse than estimated

Annual savings projection:
Old usage: 2,847 m³/year (baseline)
New usage: 2,263 m³/year (measured)
Savings: 584 m³/year = €876/year

Original estimate: €450/year
Actual performance: +95% better! 🎉

Investment: €4,200
Actual payback: 4.8 years (vs 9.3 estimated)

[Share success story] [Next improvement]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXAMPLE: Behavior Change Impact

[Baseline]
Daily electric: 12.4 kWh/day

[Change implemented: Feb 1]
Action: Smart plugs cutting standby power
Expected: -1.8 kWh/day (-€0.54/day)

[After - 2 weeks]

Bot: 📊 Behavior change results

Smart plug automation results:
Baseline standby: 2.1 kWh/day
Current standby: 0.4 kWh/day

IMPACT: -1.7 kWh/day (-81% reduction) ✅

Daily savings: €0.51
Annual projection: €186/year

Investment: €60 (3x smart plugs)
Payback: 3.9 months

Additional benefit detected:
You're checking the app daily and became
more energy-aware. Total consumption also
dropped 8% beyond standby savings!

Total impact: €245/year (vs €186 expected)

[This worked great!] [What's next?]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEATHER NORMALIZATION:

Bot automatically adjusts for weather:

Example comparison:

Week 1 (outdoor avg: 5°C): 9.2 m³/day
Week 2 (outdoor avg: -2°C): 11.8 m³/day

Naive comparison: +28% increase (alarming!)

Weather-adjusted:
Week 1: 8.9 m³/day normalized
Week 2: 9.1 m³/day normalized
True change: +2.2% (normal variance)

Bot: ✓ No significant change detected
Your usage is consistent with weather.

[View weather adjustment method]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CUMULATIVE IMPACT TRACKING:

Bot maintains running total:

[Dashboard]

YOUR OPTIMIZATION JOURNEY

Started: Jan 15, 2025
Improvements made: 5

Timeline:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Jan 22: Smart plugs installed
Impact: -€186/year ✅ Beating estimate

Feb 3: Attic insulation topped up  
Impact: -€195/year ✅ As expected

Feb 14: Wall insulation completed
Impact: -€876/year ✅ Exceeded estimate

Feb 28: Smart thermostat installed
Impact: -€145/year ✅ As expected

Mar 7: WTW ventilation system
Impact: Measuring... (2 weeks in)
Early: -€320/year ✓ On track

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CUMULATIVE RESULTS:

Total invested: €9,800
Annual savings (measured): €1,722/year
Payback: 5.7 years ← Better than 12.9 predicted!

Energy reduction: 47% (vs 39% expected)
Label improvement: D → C (measuring B now)

[View detailed timeline] [Share progress]
```

---

### 2E. Continuous Agent Interaction Examples

```
💬 ONGOING WHATSAPP CONVERSATIONS

Daily/Weekly interactions with optimization agent:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Monday 8:45 AM]

Bot: ☀️ Good morning!

Weekend summary:
Energy used: 28.4 kWh (electric), 24 m³ (gas)
Cost: €41.50
vs typical weekend: -12% ✅ Great job!

Today's weather: Sunny, high 14°C
Recommendation: Open curtains south side
                Free solar heat 10 AM - 3 PM
                Save: ~€2.80 today

[View weekend details] [Today's tips]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Tuesday 2:18 PM]

User: Why is my electric bill so high today?

Bot: Let me check your usage 🔍

Today so far (14 hours):
Electric: 18.2 kWh
Typical for this time: 9.5 kWh
Excess: +8.7 kWh (+92%!) ⚠️

Breakdown:
• 8:00-10:00 AM: Normal (2.1 kWh)
• 10:00 AM-2:00 PM: HIGH (16.1 kWh) ← Issue here

Specific spike: 10:15 AM - present
Load: 2,850W continuous for 4 hours
Cost so far: €3.42

Likely culprits:
1. Space heater? (typical: 2,000-3,000W)
2. Tumble dryer (long cycle)?
3. Water heater malfunction?

Can you check what's running since 10:15?

[I found it - space heater] [Still looking]
[Show me power graph]

User: Found it! Space heater in bedroom

Bot: Ah! For reference:
Space heater: €2.05 per day (if 24/7)
Better: Adjust central heating for that room?

Your bedroom radiator valve: Currently 40%
Outside: 8°C (mild day)

Suggestion: Increase bedroom radiator to 70%
Cost: €0.85/day (vs €2.05 space heater)
Savings: €1.20/day = €438/year

Want me to auto-adjust when cold?
[Yes, automate] [No thanks] [Tell me more]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Friday 5:42 PM]

Bot: 🎉 Weekly wins!

This week you saved:
€12.40 vs last week
€18.80 vs same week last year

Biggest win: Occupancy automation
Mon-Fri while at work: -28% heating
Savings this week: €8.20

Tips you followed:
✓ Curtains open sunny days (4/5 days)
✓ Thermostat down before bed (5/5 nights)  
✓ Dishwasher delay to off-peak (2x)

One improvement opportunity:
Wednesday 2 PM: Window open 47 minutes
                while heating active
Lost: €1.85

Weekend forecast: Cold (-1°C nights)
Recommendation: Pre-heat Sunday evening
                Guests comfortable, costs less

[View weekly report] [Set Sunday pre-heat]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Random Tuesday 11:24 PM]

Bot: 🚨 Urgent: Possible water leak

Unusual pattern detected:
Continuous water flow: 1.2 L/min
Duration: 43 minutes
Location: Unknown

This is NOT normal at 11 PM.

Possible causes:
1. Toilet running (most likely)
2. Dripping tap (large drip)
3. Pipe leak
4. Appliance malfunction

Cost if continues overnight:
Water: 432 liters (€1.73)
If hot water: +18 kWh heating (€5.40)

Please check:
[ ] Toilets (listen for running water)
[ ] Taps (all off?)
[ ] Appliances (dishwasher, washing machine?)

[I found it] [False alarm] [Need help]

User: Toilet was running! Fixed.

Bot: Great catch! 🎯

If it ran all night (8 hours):
You would have wasted:
• 576 liters water (€2.30)
• 24 kWh heating (€7.20)
• Total: €9.50

Over a year: €3,467 wasted!

These alerts have saved you €428 so far.
Small leaks add up fast.

[Good to know] [What else are you watching?]
```

---

## REQUIRED SMART HOME INTEGRATION FIELDS

```
🏠 STAGE 2 SETUP: SMART HOME CONNECTION

To enable continuous monitoring, please provide:

MONITORING SETUP:
Smart meter access:
○ P1 port adapter (enter WiFi details)
○ Energy company API (login credentials)
○ Manual entry (schedule preference)

Smart home system (if any):
○ None - will use basic monitoring only
○ Homey Pro [Connect]
○ Home Assistant [Connect]
○ Google Home [Connect]
○ Apple HomeKit [Connect]
○ Other: [Specify]

SENSORS AVAILABLE:
Temperature sensors:
[ ] Living room
[ ] Kitchen
[ ] Bedroom 1
[ ] Bedroom 2
[ ] Bathroom
[ ] Outside

Humidity sensors:
[ ] Same locations as temp

Occupancy detection:
○ Motion sensors
○ Phone geofencing
○ Manual schedule
○ None

Window/door sensors:
[ ] List locations

CONTROL CAPABILITIES:
Heating control:
○ Smart thermostat [Brand/model]
○ Smart radiator valves (TRVs) [How many]
○ Zone control [How many zones]
○ Manual only

Ventilation:
○ Smart WTW system
○ Manual control
○ None

MONITORING PREFERENCES:
Alert frequency:
○ Real-time (immediate)
○ Hourly summaries
○ Daily summaries
○ Weekly only

Alert types:
[ ] Energy leaks/spikes
[ ] Temperature anomalies
[ ] Cost thresholds
[ ] Efficiency drops
[ ] Behavioral tips
[ ] Weekly reports

[Save Preferences] [Test Connection]
```

---

**Section Added**: Complete Two-Stage Intelligence System
**Stage 1**: Statistical thermal analysis, anomaly detection, benchmarking
**Stage 2**: Continuous monitoring, automated leak detection, smart home integration
**Key Features**:
- Real-time energy monitoring (10-second intervals)
- Automated thermal leak detection
- Occupancy-based heating control
- Multi-zone climate optimization
- Weather-normalized effect measurement
- Continuous WhatsApp interaction
- Smart home system integration (Homey, Home Assistant, Google, Apple)
**Investment**: €60-€1,500 depending on smart home tier
**Typical Savings**: €350-€900/year from optimization alone
**Payback**: 3-25 months for monitoring equipment

