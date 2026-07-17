#!/usr/bin/env python3
import sys, json, time
from datetime import datetime

# Rough phone energy model (can be calibrated later with real battery logs)
JOULES_PER_SECOND_CPU = 1.8   # very rough for A15-class SoC under load

def measure(prompt, model="local", tokens_out=0, latency_s=0.0, usefulness=0.8):
    tokens_in = len(prompt.split()) * 1.3   # rough
    joules = latency_s * JOULES_PER_SECOND_CPU
    comp_ability_per_token = (usefulness * max(tokens_out, 1)) / max(joules, 0.001)
    return {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "tokens_in": int(tokens_in),
        "tokens_out": tokens_out,
        "latency_s": round(latency_s, 2),
        "approx_joules": round(joules, 2),
        "usefulness": usefulness,
        "comp_ability_per_token": round(comp_ability_per_token, 4),
        "node": "N0_measure_llm_efficiency"
    }

if __name__ == "__main__":
    # Example usage
    result = measure(
        prompt="increase solar thermal capture area for PoPW",
        model="gemma-local",
        tokens_out=180,
        latency_s=4.2,
        usefulness=0.85
    )
    print(json.dumps(result, indent=2))
