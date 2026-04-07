import marimo

__generated_with = "0.22.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import importlib.util
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    from pathlib import Path

    return Path, go, importlib, mo, np


@app.cell
def _(Path, importlib):
    model_path = Path.cwd() / "ai_human_token_model" / "model.py"
    if not model_path.exists():
        model_path = Path.cwd().parent / "ai_human_token_model" / "model.py"
    spec = importlib.util.spec_from_file_location("ai_human_token_model.model", model_path)
    if spec is None or spec.loader is None:
        raise ModuleNotFoundError(f"Unable to load model module from {model_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    AIHumanTokenModel = module.AIHumanTokenModel
    return (AIHumanTokenModel,)


@app.cell
def _(mo):
    title = mo.md("# AI-Human Token Dynamics\n**Interactive Consumer-Resource Model**")
    explanation = mo.md(
        """
    ### Relationship to Predator-Prey / Consumer-Resource Models
    This system maps AI production and human processing onto **consumer-resource dynamics** (a standard extension of classic Lotka-Volterra predator-prey models):
    - **Resource (prey-like)**: Backlog of unprocessed tokens $(U)$
    - **Consumers**: Humans $(H)$, limited by attention and handling time
    - Production and consumption both use **Holling type II** saturation terms
    The model produces natural self-regulation and diminishing returns with team size.
    """
    )
    return explanation, title


@app.cell
def _(mo):
    intro = mo.md("Adjust parameters and choose simulation type below.")
    H = mo.ui.slider(1, 20, value=5, step=1, label="Number of humans (H)")
    alpha = mo.ui.slider(500, 5000, value=1800, step=100, label="α: tokens per prompt")
    beta = mo.ui.slider(
        200, 1500, value=650, step=25, label="β: processing tokens/hr per human"
    )
    gamma = mo.ui.slider(5, 30, value=12, label="γ: max prompts/hr per human")
    K = mo.ui.slider(
        2000, 30000, value=12000, step=1000, label="K: prompting half-saturation"
    )
    M = mo.ui.slider(
        1000, 20000, value=6000, step=500, label="M: processing half-saturation"
    )
    simulation_type = mo.ui.dropdown(
        options=["Continuous (ODE)", "Discrete Euler", "Discrete Map"],
        value="Continuous (ODE)",
        label="Simulation type",
    )
    controls = mo.vstack(
        [
            intro,
            mo.hstack([H, alpha], widths="equal"),
            mo.hstack([beta, gamma], widths="equal"),
            mo.hstack([K, M], widths="equal"),
            simulation_type,
        ]
    )
    return H, K, M, alpha, beta, controls, gamma, simulation_type


@app.cell
def _(AIHumanTokenModel, H, K, M, alpha, beta, gamma, mo, np, simulation_type):
    model = AIHumanTokenModel(
        H=H.value,
        alpha=alpha.value,
        beta=beta.value,
        gamma=gamma.value,
        K=K.value,
        M=M.value,
    )

    if simulation_type.value == "Continuous (ODE)":
        t, U = model.simulate_continuous()
        title_suffix = ""
    elif simulation_type.value == "Discrete Euler":
        t, U = model.simulate_discrete_euler(steps=300, dt=1.0)
        title_suffix = " — Discrete Euler"
    else:
        t, U = model.simulate_discrete_map(steps=300)
        title_suffix = " — Discrete Map"

    time_fig = mo.ui.plotly(model.create_time_series_plot(t, U, title_suffix))

    Ustar, throughput = model.get_equilibrium()
    equilibrium = mo.md(
        f"**Equilibrium backlog**: {Ustar:,.0f} tokens  **Steady-state throughput**: {throughput:,.0f} tokens/hour"
    )

    Hs = np.arange(1, 21)
    scaling_fig = mo.ui.plotly(model.create_scaling_plot(Hs))

    notes = mo.md(
        """
    **Simulation types**  
    • **Continuous (ODE)** — smooth numerical integration  
    • **Discrete Euler** — step-by-step with explicit dt  
    • **Discrete Map** — simplest one-step update $U_{n+1} = U_n + r(U_n)$
    All methods converge to the same equilibrium. Hover, zoom, and pan the interactive plots to explore the dynamics!
    """
    )
    return equilibrium, notes, scaling_fig, time_fig


@app.cell
def _(
    controls,
    equilibrium,
    explanation,
    mo,
    notes,
    scaling_fig,
    time_fig,
    title,
):
    mo.vstack([title, explanation, controls, time_fig, equilibrium, scaling_fig, notes])
    return


if __name__ == "__main__":
    app.run()
