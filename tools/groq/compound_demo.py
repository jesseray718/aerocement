#!/usr/bin/env python3
"""
compound_demo.py — OpenRoot agentic examples (fixed import for Termux/repo).
Self-bootstraps sys.path so `python3 tools/groq/compound_demo.py` works from openroot/ root.
Uses prior GroqCascade. Demonstrates groq/compound-mini (fast single tool) + compound (multi).

H-003 thermal math, Black Locust yield model, aerocement lookup.
Parses executed_tools[] + usage_breakdown{} for audit/PoPW trail.

Run once: export GROQ_API_KEY=sk-... then python3 tools/groq/compound_demo.py
Only 1 compound call on default run (conserves 250 RPD quota). Uncomment others for full exploration.
"""

import sys
from pathlib import Path

# Bootstrap: go up from tools/groq/compound_demo.py → openroot root so "from tools.groq..." works
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.groq.groq_cascade import GroqCascade


def print_tool_audit(resp: dict) -> None:
    msg = resp.get("choices", [{}])[0].get("message", {})
    tools = msg.get("executed_tools", [])
    if not tools:
        print("No tools executed (pure text path).")
        return
    for t in tools:
        ttype = t.get("type", "?")
        args = t.get("args", {})
        result = str(t.get("result", ""))[:120].replace("\n", " ")
        print(f"TOOL {ttype} | args={args} | result_preview={result}...")


def print_usage_breakdown(resp: dict) -> None:
    ub = resp.get("usage_breakdown", {})
    for m in ub.get("models", []):
        mid = m.get("model", "?")
        u = m.get("usage", {})
        print(f"  SUB {mid}: prompt {u.get('prompt_tokens',0)} tok / {u.get('prompt_time',0):.3f}s | "
              f"completion {u.get('completion_tokens',0)} tok / {u.get('completion_time',0):.3f}s")


def run_compound(prompt: str, use_mini: bool = False) -> dict:
    model = "groq/compound-mini" if use_mini else "groq/compound"
    client = GroqCascade(cascade=[model])
    return client.chat_completions_create(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.2,
    )


if __name__ == "__main__":
    print("=== H-003 THERMAL MATH (code_interpreter via compound-mini) ===")
    p1 = ("Using code execution only, calculate total kWh captured over 7 nights "
          "for 10m2 H-003 at 12.91 kWh/m2 nightly. Show the exact formula and final number.")
    r1 = run_compound(p1, use_mini=True)
    print(r1["choices"][0]["message"]["content"])
    print_tool_audit(r1)
    print_usage_breakdown(r1)

    # Uncomment below only after first run succeeds and you have quota headroom (compound = 250 RPD)
    # print("\n=== PERMACULTURE + YIELD MODEL (search + code via compound) ===")
    # p2 = ("Web search current Black Locust permaculture yields and soil benefits "
    #       "in Missouri for vertical quail integration. Then code-estimate annual food lbs from 50 trees.")
    # r2 = run_compound(p2, use_mini=False)
    # print(r2["choices"][0]["message"]["content"])
    # print_tool_audit(r2)
    # print_usage_breakdown(r2)
