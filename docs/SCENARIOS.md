# Scenario Presets

This document provides parameter sets that should produce clearly different qualitative behaviours in the AI-Human Token Dynamics model.

Each scenario uses:
- `H`: number of humans
- `alpha`: tokens per prompt
- `beta`: processing tokens/hour per human
- `gamma`: max prompts/hour per human
- `K`: prompting half-saturation
- `M`: processing half-saturation
- `U0`: initial backlog

Use these as starting points, then tune around them.

## 1) Near-balanced steady state

Purpose: show a stable operating regime where backlog settles without severe growth.

- `H = 8`
- `alpha = 1000`
- `beta = 1000`
- `gamma = 10`
- `K = 12000`
- `M = 6000`
- `U0 = 500`

Expected behaviour:
- backlog may rise initially, then flatten
- equilibrium backlog is moderate
- throughput is stable and near production rate

## 2) Persistent overload (backlog runaway)

Purpose: demonstrate what happens when AI generation outpaces human processing capacity.

- `H = 4`
- `alpha = 2600`
- `beta = 550`
- `gamma = 14`
- `K = 20000`
- `M = 7000`
- `U0 = 500`

Expected behaviour:
- sustained backlog growth over time
- no practical convergence in the displayed horizon
- increasing pressure on review/consumption capacity

## 3) Human-constrained low-output regime

Purpose: show low generation pressure where backlog remains low and output is conservative.

- `H = 3`
- `alpha = 700`
- `beta = 900`
- `gamma = 7`
- `K = 8000`
- `M = 5000`
- `U0 = 200`

Expected behaviour:
- backlog stays low or slowly declines
- lower steady throughput than high-output scenarios
- high stability, low stress regime

## 4) Fast saturation with diminishing returns

Purpose: show how large team size does not produce linear gains because saturation terms dominate.

- `H = 16`
- `alpha = 1800`
- `beta = 650`
- `gamma = 12`
- `K = 12000`
- `M = 6000`
- `U0 = 600`

Expected behaviour:
- higher throughput than small teams, but sub-linear scaling
- equilibrium backlog still non-trivial
- clear diminishing returns in scaling plot

## 5) Recovery from high initial backlog

Purpose: show a regime where a large starting queue can still be brought under control.

- `H = 10`
- `alpha = 1100`
- `beta = 950`
- `gamma = 10`
- `K = 14000`
- `M = 6000`
- `U0 = 12000`

Expected behaviour:
- backlog declines after initial transient period
- eventual convergence toward a lower equilibrium
- useful for illustrating catch-up dynamics

## 6) Discrete-mode divergence contrast

Purpose: compare continuous vs discrete behaviour under the same settings.

- `H = 5`
- `alpha = 1800`
- `beta = 650`
- `gamma = 12`
- `K = 12000`
- `M = 6000`
- `U0 = 200`

Expected behaviour:
- continuous (ODE) appears smooth and convergent
- discrete Euler and discrete map show stronger step effects
- useful for discussing modelling assumptions and time granularity

## Recommended usage in demos

1. Start with Scenario 1 (baseline).
2. Jump to Scenario 2 (failure mode).
3. Show Scenario 5 (recovery path).
4. Finish with Scenario 4 (scaling limits).

This sequence communicates stability, risk, mitigation, and limits in a concise narrative.
