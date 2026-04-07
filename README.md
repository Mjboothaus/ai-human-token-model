# ai-human-token-model

AI-Human Token Model

# AI-Human Token Dynamics

An interactive **consumer-resource model** (inspired by predator-prey mathematics) that simulates the dynamics between AI token production and human processing capacity.

## What is this?

This project models a common real-world situation in AI-assisted workflows:

- AI tools generate large volumes of output (tokens, text, code, analysis, etc.) very quickly.
- Humans must prompt the AI **and** process/consume the resulting output.
- Human time and attention are limited, creating a natural **bottleneck**.

The model captures the feedback loop: when the backlog of unprocessed tokens grows, humans spend more time reading/editing and less time prompting, which slows new production. This self-regulating behavior mirrors **consumer-resource dynamics** from ecology.

**Key variables**:
- `U(t)` — backlog of unprocessed tokens (the "resource")
- `H` — number of humans (the "consumers")
- `α` — tokens generated per prompt
- `β` — maximum tokens one human can usefully process per hour
- `γ` — maximum prompts one human can issue per hour (when not overwhelmed)
- Saturation constants `K` and `M` that create realistic handling-time limits (Holling type II functional responses)

The system naturally shows:
- Stable throughput when balanced
- Exploding or very large backlogs when under-resourced
- Diminishing returns as you add more humans or make AI faster

## Why this model?

Traditional productivity thinking often assumes linear scaling ("faster AI = more output"). In reality, human cognitive and time constraints create nonlinear dynamics, saturation, and feedback loops.

This model helps answer questions such as:
- How many humans do we need to keep the backlog manageable?
- What happens to overall throughput when we make the AI much faster (higher `α`)?
- Where are the real bottlenecks in AI-augmented teams?
- How does team size affect equilibrium backlog vs. useful output?

It is grounded in well-established **consumer-resource theory** (extensions of Lotka-Volterra predator-prey models) and aligns with current research on human-AI collaboration, cognitive load in LLM workflows, and productivity bottlenecks.

Use cases include:
- Planning AI adoption in knowledge-work teams
- Estimating required human support for AI agents or copilots
- Teaching dynamical systems / operations research with a relatable modern example
- Exploring "paradox of enrichment" effects (making the AI richer can sometimes destabilize workflow)

## How to run it

### Prerequisites
```bash
pip install marimo numpy scipy plotly
```

Quick start

Save the main file as ai_human_token_dynamics.py
Run the notebook:BashCopymarimo run ai_human_token_dynamics.py
Open the URL shown in your terminal (usually http://localhost:2718)

The interface includes:

Sliders for all model parameters
Choice between Continuous (ODE), Discrete Euler, and Discrete Map simulations
Interactive Plotly charts (hover, zoom, pan)
Live equilibrium calculations (backlog and steady-state throughput)
Scaling plots showing behavior as the number of humans changes

Files

ai_human_token_dynamics.py — the complete interactive Marimo notebook (self-contained)

Model Structure
The core rate equation is:
$$\frac{dU}{dt} = \alpha \cdot \gamma H \cdot \frac{K}{K + U} - \beta H \cdot \frac{U}{U + M}
$$

Three simulation methods are provided:

Continuous (ODE) — smooth numerical integration (most accurate)
Discrete Euler — step-by-step with explicit time step
Discrete Map — simplest iterative map (U_{n+1} = U_n + rate(U_n)), ideal for hourly or batch thinking

All methods converge to the same equilibrium.

References

See the separate REFERENCES.md (or the References section in the notebook) for foundational consumer-resource papers, Holling type II literature, and recent human-AI collaboration studies.

Extending the model

Easy next steps:

Add time delays → can produce oscillations (true predator-prey style cycles)
Introduce stochastic noise in the discrete map
Model multiple AI tools or quality degradation
Add a second state variable (e.g., "human prompt quality" or "cumulative knowledge")
Export simulation results or add parameter optimisation