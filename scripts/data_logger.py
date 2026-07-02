#!/usr/bin/env python3
"""
Aerocement Prototype V1 Data Logger
Termux-compatible. Logs temperature and humidity to CSV.

Replace stub functions with real sensor reads (DS18B20, DHT22, etc).
"""

import time
import csv
import os
from datetime import datetime

LOG_DIR = os.path.expanduser("~/aerocement/data")
LOG_FILE = os.path.join(LOG_DIR, "log.csv")

SENSORS = {
    "T1": "Tunnel intake",
    "T2": "After desiccant",
    "T3": "Tunnel outlet",
    "T4": "Cooler interior",
    "T5": "Solar outlet",
}

HYGROMETERS = {
    "H1": "Before desiccant",
    "H2": "After desiccant",
}


def read_temp(sensor_id):
    """Replace with real DS18B20 read."""
    return 25.0 + (time.time() % 10)  # SIMULATED


def read_humidity(sensor_id):
    """Replace with real DHT22 read."""
    return 50.0 + (time.time() % 20)  # SIMULATED


def main():
    os.makedirs(LOG_DIR, exist_ok=True)
    header = ["timestamp"] + list(SENSORS.keys()) + list(HYGROMETERS.keys())

    print(f"Logging to {LOG_FILE}")
    print(f"Sensors: {header}")

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if os.path.getsize(LOG_FILE) == 0:
            writer.writerow(header)

        while True:
            row = [datetime.now().isoformat()]
            row += [read_temp(sid) for sid in SENSORS]
            row += [read_humidity(hid) for hid in HYGROMETERS]
            writer.writerow(row)
            f.flush()
            print(f"  {row[0]} | T1={row[1]:.1f} T2={row[2]:.1f} T3={row[3]:.1f} T4={row[4]:.1f} T5={row[5]:.1f} H1={row[6]:.1f} H2={row[7]:.1f}")
            time.sleep(60)


if __name__ == "__main__":
    main()
