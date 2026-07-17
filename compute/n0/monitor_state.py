#!/usr/bin/env python3
import json, os, subprocess
from datetime import datetime

def get_cpu():
    try:
        with open('/proc/stat') as f:
            line = f.readline()
        fields = [float(x) for x in line.split()[1:]]
        return round(sum(fields[0:3]) / sum(fields) * 100, 1)
    except:
        return 0.0

def get_ram():
    try:
        with open('/proc/meminfo') as f:
            lines = f.readlines()
        total = int(lines[0].split()[1])
        avail = int(lines[2].split()[1])
        return round((total - avail) / total * 100, 1)
    except:
        return 0.0

battery = 0
try:
    out = subprocess.check_output(['termux-battery-status'], text=True)
    battery = json.loads(out).get('percentage', 0)
except:
    pass

state = {
    "timestamp": datetime.now().isoformat(),
    "cpu_percent": get_cpu(),
    "ram_percent": get_ram(),
    "battery_percent": battery,
    "node": "N0_monitor_state_termux"
}
print(json.dumps(state, indent=2))
