# NEXT STEPS

This document captures practical enhancements and extension options for the `ai-human-token-model` project.

## 1) Immediate Enhancements (short term)

### 1.1 Improve notebook usability
- Add preset scenario buttons (e.g. “balanced team”, “AI-heavy”, “review bottleneck”).
- Add parameter reset controls and clear tooltips for each slider.
- Add optional axis normalisation to compare runs more easily.

### 1.2 Strengthen output interpretability
- Add derived metrics panel:
  - backlog growth rate
  - time-to-equilibrium
  - utilisation proxy for human processing load
- Add concise “model interpretation” text that updates with current settings.

### 1.3 Improve simulation controls
- Expose simulation horizon and timestep directly in the UI.
- Add an option to overlay multiple runs for side-by-side comparison.
- Add CSV export of simulation traces for external analysis.

## 2) Model Extensions (near term)

### 2.1 Add delay and lag effects
- Introduce response delays between backlog growth and behaviour change.
- Evaluate whether delays produce oscillations/cycles under realistic parameters.

### 2.2 Add stochastic dynamics
- Add optional noise terms for prompt generation and processing variability.
- Compare deterministic vs stochastic outcomes under identical settings.

### 2.3 Expand state representation
- Add a second state variable for quality (e.g. review quality score or defect backlog).
- Model trade-offs between throughput and quality under increased load.

### 2.4 Kolmogorov-style generalised dynamics (optional mode)
- Introduce a generalised formulation with per-capita rates:
  - `dU/dt = U * F(U, H, ...)` or equivalent production-consumption decomposition with flexible `F`/`G` terms.
- Keep current model as default and expose this as an advanced toggle.
- Allow selection of alternative functional forms (e.g. stronger saturation, threshold effects, interference terms).
- Use this mode for stress testing nonlinear behaviours and checking robustness of conclusions from the baseline model.

## 3) Calibration and Validation

### 3.1 Parameter calibration workflow
- Define a reproducible workflow for calibrating `alpha`, `beta`, `gamma`, `K`, and `M` from observed team metrics.
- Add a simple notebook section that estimates parameters from sample data.

### 3.2 Sensitivity analysis
- Run one-at-a-time and global sensitivity checks across parameter ranges.
- Identify the most influential parameters for backlog stability and throughput.

### 3.3 Scenario testing pack
- Create a small benchmark scenario set with expected qualitative behaviour.
- Use this pack as a regression baseline after model changes.

## 4) Engineering and Project Quality

### 4.1 Testing and checks
- Add tests for core model methods (`rate`, simulations, equilibrium solver).
- Add a `just test` recipe once a test framework is introduced.
- Add a `just check` recipe that runs formatting/lint/tests in one command.

### 4.2 Code structure
- Consider separating model logic from notebook UI for maintainability.
- Introduce a small `src/` package if the model grows beyond notebook scope.

### 4.3 Documentation
- Add an assumptions and limitations section to the README.
- Add a concise glossary for model terms and symbols.
- Add reproducibility notes for environment setup and versions.

## 5) Practical Adoption Extensions

### 5.1 Decision-support outputs
- Add a recommendation layer that suggests staffing or parameter adjustments.
- Add threshold-based alerts (e.g. “backlog risk high”).

### 5.2 Governance and people-risk integration
- Add explicit indicators for human load and review pressure.
- Add a “safe operating zone” view linking throughput and people-risk constraints.

### 5.3 Optional deployment path
- Package as a lightweight web app for broader stakeholder use.
- Add a static report generator for scenario comparisons.

## 6) Suggested Execution Order

1. UX and interpretability upgrades in the marimo notebook.
2. Export + scenario comparison features.
3. Testing baseline and scenario regression pack.
4. Stochastic and delay model extensions.
5. Calibration workflow and decision-support layer.
