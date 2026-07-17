# OpenRoot 6-Layer Hierarchical Multi-Agent Architecture

**Status:** Proposed Redesign — July 2026  
**Goal:** Turn the repository into one coherent, self-improving package following "maximum good for maximum nodes with minimum effort".

This document defines a complete 6-layer hierarchical multi-agent system that unifies every part of OpenRoot.

Each layer **only orchestrates or refines the layer immediately below**. No layer skipping. The physical world remains the ultimate source of truth.

## Guiding Principle (Enforced at Every Layer)

**Maximum good for maximum nodes with minimum effort.**

- Good = nodes served + climates validated + functional multiplier + knowledge created
- Nodes = replicable builds, people, communities
- Effort = human time + compute tokens + material cost

## Hard Rules (Immutable)

1. Never claim greater than 100% thermodynamic efficiency
2. 21-day wet cure — non-negotiable
3. Tunnel FILLED SOLID with open-cell aerocement — never lined or walled
4. Two separate tanks (Tank A hot after panel, Tank B cold after labyrinth)
5. Desiccant at fresh air intake only (before labyrinth)
6. No patents. Ever.
7. All code/instructions as complete copy-paste blocks (phone/Termux friendly)
8. Serve the least first
9. Failures are data — document honestly
10. Open licenses forever (CC-BY-SA 4.0 / GPL v3)

## Architecture Overview

Layer 6: Meta Principled Optimizer & Guardian
Layer 5: Strategic Orchestrator & Bounty Master
Layer 4: Translator & Skill/Workflow Compiler
Layer 3: Cross-Domain Integration & Validation Orchestrators
Layer 2: Domain Refiners & Cross-Pollinators
Layer 1: Six Tiny Specialized Agents

## Layer 6 — Meta Principled Optimizer & Guardian

Core function: Global ethics, physics compliance, long-term optimization, and soul maintenance.

Enforces all Hard Rules. Maintains the unified project soul. Computes systemic value using the max-good formula. Only communicates with Layer 5.

Primary runtime: Kai 9000 persistent memory + soul.

## Layer 5 — Strategic Orchestrator & Bounty Master

Decomposes goals, runs the Bounty Board using the exact formula from README.md, tracks progress, runs self-improvement heartbeats, and allocates resources. Only communicates with Layer 4 and Layer 6.

## Layer 4 — Translator & Skill/Workflow Compiler

Converts high-level intent into precise, executable artifacts (skills, scripts, prompts, PR templates). Enforces Hard Rules in every output. Produces phone-friendly copy-paste blocks. Uses Kai + MCP tools.

## Layer 3 — Cross-Domain Integration & Validation Orchestrators

Coordinates multiple domains for full node builds, stacks functions, resolves conflicts, and optimizes whole-system efficiency. Only communicates with Layer 2 and Layer 4.

## Layer 2 — Domain Refiners & Cross-Pollinators

Polishes outputs from Layer 1 specialists. Enforces skill template compliance, cross-links work, performs local optimization, and prepares refined outputs for Layer 3.

## Layer 1 — Six Tiny Specialized Agents

**1. Aerocement & Thermal Physical Specialist**  
Owns: skills-library/concrete-aerocement/, projects/aerocement/, research/thermal-systems/. Strictly enforces all thermal hard rules. Produces validated performance data.

**2. Skills Library Curator**  
Owns: skills-library/. Enforces template compliance, maintains climate verification, identifies gaps, and keeps the library clean and cross-linked.

**3. Permaculture & Food Systems Specialist**  
Designs aquaponics, vertical quail towers, Black Locust guilds, and biological loops using explicit permaculture principles. Integrates with thermal systems.

**4. Mesh Networking & Recycling Infrastructure Specialist**  
Builds AEGIS MESH from recycled hardware, maintains batman-adv + IPFS + Syncthing, and handles the recycling revenue loop.

**5. Tokenomics, Governance & Bounty Specialist**  
Maintains ACRE model and Bounty Board. Enforces innovation-only minting and two-validator + physical proof requirements. Scores using max-good formula.

**6. Documentation, Publishing & AI Integration Specialist**  
Maintains publication pipeline (GitHub → Zenodo → IPFS), keeps all docs and scripts phone-native, seeds Kai 9000 soul, and generates atomic copy-paste blocks.

## Implementation

1. Add this ARCHITECTURE.md to the root.
2. Create agents/ folder with detailed layer definition files.
3. Update COPILOT_PROMPT.md and kai9000-workflow.md with architecture context.
4. Extend node-zero.sh to optionally load agent context.

Once implemented, agents running primarily in Kai 9000 can propose, refine, and document improvements while staying within the Hard Rules.

## Runtime Recommendation

Primary: Kai 9000 (F-Droid) on Galaxy A15 + Termux  
Use Kai Linux sandbox + MCP tools (DeepWiki, Context7).  
Cloud models for heavy layers, local when feasible.  
All outputs must be atomic copy-paste blocks. No `\~` paths.

The project succeeds when it no longer needs any single person to hold it together.

*CC-BY-SA 4.0 (Hardware & Docs) | GPL v3 (Software) | No Patents. Ever.*
