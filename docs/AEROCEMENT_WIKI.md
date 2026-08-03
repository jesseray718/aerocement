# AeroCement — Canonical Wiki
## Volumetric Open-Cell Blackbody Concrete as Triple-Utility Infrastructure

**η-law**: useful_joules / human_joules. Every claim below is scored against that metric.

### 1. Material Definition
AE-GFRC (Aerated Glass-Fiber Reinforced Concrete) with activated-carbon / zirconium substitution.
- Open-cell porosity engineered 60-80 % for forced convection through the bulk, not over a surface.
- Volumetric blackbody absorption of incident solar radiation: measured/simulated first-pass 95-98 %.
- Glass fiber provides tensile capacity without steel rebar (eliminates corrosion and thermal bridging).
- Low-pressure pneumatic pumpability (higher volume, lower pressure than conventional concrete).
- Local materials only: cement or geopolymer binder, sand, aggregate, water, scrap fiber, activated carbon, optional zirconium.

This is not surface-coated concrete. The entire thickness is the absorber and the heat-exchange matrix.

### 2. Triple Utility (the η multiplier)
One physical object simultaneously delivers:
1. **Structural** — load-bearing walls, floors, labyrinth, dome skin.
2. **Thermal transport** — air is drawn *through* the open-cell matrix; pore-scale surface area produces high Nusselt-number heat transfer with minimal fan power.
3. **Energy capture & storage** — 12.91 kWh_th / m² / night (simulation, H-003 Rev-C); multi-day ground-battery retention at \~1.056 kWh/day passive loss.

Functional multiplier ≈ 2.2× relative to a conventional insulated wall that only provides structure. When the same mass also drives Stirling/TEG discharge, the system produces both heat and shaft work / electricity from the same solar input.

### 3. System Architecture (open-loop, zero circulating fluid)
Sun → Volumetric Panel (98 % capture) → Underground Labyrinth (open-cell pores force contact) → Insulated Ground Battery → Stirling / TEG Discharge → Exhaust to atmosphere → optional night-sky radiative pre-cooling of inlet air.

No sealed loops. No antifreeze. No pumps in the primary cycle (optional low-power assist only). The concrete *is* the heat exchanger, the storage medium, and the structure.

### 4. Full-Utilization Potential (what happens when the material is taken seriously)
- **Every wall becomes a collector.** Roof and south façade cease to be dead mass and become active thermal surfaces. Building envelope η rises dramatically.
- **Ground battery as free seasonal storage.** Multi-day to multi-week thermal flywheel using only soil + concrete mass. Night-time power and daytime cooling without batteries or grid.
- **PoPW / ACRE coupling.** Verified installed thermal capacity (kWh_th capacity, measured ΔT and airflow) mints real tokens. Physical work is the collateral. No pure computational PoW.
- **Zero-OPEX shelter + energy + food stack.** Pair with Black Locust RMH, geodesic aerocement domes, vertical quail/aquaponics. One material system closes energy, shelter, and protein loops.
- **Low-resource deployability.** Drill-and-bucket or pneumatic placement. 21-day wet cure. Local aggregates. No exotic supply chain after the first activated-carbon and fiber batch.
- **Defensive publication + open replication.** CC-BY-SA hardware / GPL-3.0 software. Zenodo + IPFS mirrors already exist. Anyone can reproduce the pore geometry and the thermal cascade.

If scaled to district level, the marginal cost of additional thermal capacity approaches the cost of the concrete itself. Human joules are front-loaded in formwork and first pour; thereafter the system runs on solar joules with near-zero maintenance.

### 5. Current Validation State (2026-08)
- Simulation (thermal_cascade_v2.py) complete and dataset published (Zenodo 10.5281/zenodo.21225683).
- H-001 pneumatic pumpability validated.
- H-003 thermal cascade active (labyrinth + discharge path).
- Physical prototype and independent replication still required.
- Open peer-review questions remain on realistic Carnot ceiling (sky temperature, not 3 K), pore-scale CFD Nusselt number, and exact AE-GFRC pump-pressure curves.

### 6. Next Physical Actions (η-ranked)
1. Instrument first 1 m² panel + short labyrinth section with ΔT, airflow, and pressure-drop sensors. Write only measured joules into the ledger.
2. Lock Micro-Node dimensions and mix design that hits target porosity + strength.
3. Wire measured capacity → ACRE minting path.
4. Push this wiki + SPEC-H003 + dataset into every mirror (GitHub, IPFS, Appropedia, local nodes).

### 7. Licensing & Attribution
Docs & hardware designs: CC-BY-SA-4.0  
Code: GPL-3.0  
Collective copyright: One Human Family  
Co-authorship offered for measured data or validated models that raise η.

### 8. Canonical Locations
- Thermal repo: https://github.com/jesseray718/aerocement
- Main ecosystem: https://github.com/jesseray718/openroot
- Appropedia: https://www.appropedia.org/Aerocement
- Dataset: https://doi.org/10.5281/zenodo.21225683
- This file: docs/AEROCEMENT_WIKI.md (source of truth for the wiki narrative)

Generated / consolidated 2026-08-02.  
Update only with measured data or peer-reviewed corrections.
