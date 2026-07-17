import json
import math

# Rocket Mass Heater + Molten Salt Thermal Storage Vehicle Model
# Hot side: RMH with molten salt at T_hot
# Cold side: ambient airflow radiator at T_cold
# Fuel: coppiced black locust (carbon-negative)

# --- Parameters ---
T_hot = 538 + 273.15      # molten salt max temp (°C → K), typical solar salt
T_cold = 293.15           # ambient air (~20°C)
stirling_eff = 0.35        # Stirling engine mechanical efficiency
gen_eff = 0.92             # alternator efficiency
motor_eff = 0.90           # electric motor efficiency
salt_cp = 1530             # J/(kg·K) molten salt specific heat
salt_mass = 150            # kg of molten salt onboard
black_locust_LHV = 19.5e6  # J/kg dry black locust lower heating value
burn_rate = 2.5            # kg/h fuel consumption
rmh_eff = 0.85             # rocket mass heater combustion+transfer efficiency

# --- Carnot ceiling ---
carnot = 1 - (T_cold / T_hot)

# --- Energy available in salt reservoir ---
dT = T_hot - T_cold
salt_energy = salt_mass * salt_cp * dT  # Joules stored

# --- RMH thermal input ---
rmh_thermal_power = burn_rate * black_locust_LHV * rmh_eff / 3600  # Watts

# --- Stirling shaft power ---
stirling_shaft = rmh_thermal_power * stirling_eff

# --- Wheel power ---
wheel_power = stirling_shaft * gen_eff * motor_eff

# --- Range estimate (assume 5 kW average draw at wheels) ---
avg_draw = 5000  # Watts
range_hours = salt_energy / (avg_draw / (stirling_eff * gen_eff * motor_eff)) / 3600
range_km = range_hours * 45  # assume 45 km/h avg

results = {
    "carnot_ceiling": round(carnot * 100, 2),
    "rmh_thermal_kw": round(rmh_thermal_power / 1000, 2),
    "stirling_shaft_kw": round(stirling_shaft / 1000, 2),
    "wheel_power_kw": round(wheel_power / 1000, 2),
    "salt_storage_kwh": round(salt_energy / 3.6e6, 2),
    "est_range_hours": round(range_hours, 2),
    "est_range_km": round(range_km, 1),
    "fuel_rate_kg_h": burn_rate,
    "fuel_carbon_status": "carbon-negative (coppice roots sequester)"
}

print(json.dumps(results, indent=2))

with open("/data/data/com.termux/files/home/openroot/rmh_results.json", "w") as f:
    json.dump(results, f, indent=2)
