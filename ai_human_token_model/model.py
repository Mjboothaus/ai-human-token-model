import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.integrate import odeint
from scipy.optimize import fsolve


class AIHumanTokenModel:
    """Model of AI token production vs human processing capacity.

    Consumer-resource dynamical system (close relative of predator-prey models).
    """

    def __init__(
        self,
        H: float = 5,
        alpha: float = 1800,
        beta: float = 650,
        gamma: float = 12,
        K: float = 12000,
        M: float = 6000,
    ):
        self.H = H
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.K = K
        self.M = M

    def rate(self, U: float, t: float = 0) -> float:
        """Core rate of change of backlog."""
        prompt_rate = self.gamma * self.H * (self.K / (self.K + U))
        production = self.alpha * prompt_rate
        consumption = self.beta * self.H * (U / (U + self.M))
        return production - consumption

    def simulate_continuous(
        self, U0: float = 200.0, t_max: float = 96, n_points: int = 1200
    ):
        """Continuous ODE solution."""
        t = np.linspace(0, t_max, n_points)
        sol = odeint(self.rate, U0, t, atol=1e-8, rtol=1e-8)
        return t, sol.flatten()

    def simulate_discrete_euler(
        self, U0: float = 200.0, steps: int = 300, dt: float = 1.0
    ):
        """Discrete Euler integration."""
        U = np.zeros(steps)
        U[0] = U0
        for i in range(1, steps):
            dU = self.rate(U[i - 1]) * dt
            U[i] = max(0.0, U[i - 1] + dU)
        t = np.arange(steps) * dt
        return t, U

    def simulate_discrete_map(self, U0: float = 200.0, steps: int = 300):
        """True discrete map (each step = 1 hour)."""
        U = np.zeros(steps)
        U[0] = U0
        for i in range(1, steps):
            delta = self.rate(U[i - 1])
            U[i] = max(0.0, U[i - 1] + delta)
        t = np.arange(steps)
        return t, U

    def get_equilibrium(self):
        """Steady-state backlog and throughput."""

        def equilibrium_eq(U):
            return self.rate(U[0])

        Ustar = fsolve(equilibrium_eq, [1000.0])[0]
        Ustar = max(Ustar, 0.0)
        throughput = self.beta * self.H * (Ustar / (Ustar + self.M))
        return Ustar, throughput

    def create_time_series_plot(self, t, U, title_suffix=""):
        """Interactive Plotly line plot for backlog evolution."""
        fig = px.line(
            x=t,
            y=U,
            labels={"x": "Time (hours or steps)", "y": "Backlog U — unprocessed tokens"},
            title=f"Backlog Evolution (H = {self.H:.0f}){title_suffix}",
            line_shape="linear",
        )
        fig.update_traces(line_color="royalblue", line_width=3)
        fig.update_layout(hovermode="x unified", template="plotly_white", height=450)
        return fig

    def create_scaling_plot(self, Hs: np.ndarray):
        """Interactive side-by-side Plotly subplots for scaling behaviour."""
        Ustars = []
        throughputs = []
        for h in Hs:
            temp = AIHumanTokenModel(h, self.alpha, self.beta, self.gamma, self.K, self.M)
            u, th = temp.get_equilibrium()
            Ustars.append(u)
            throughputs.append(th)

        fig = make_subplots(
            rows=1,
            cols=2,
            subplot_titles=("Backlog vs Team Size", "Useful Output vs Team Size"),
        )

        fig.add_trace(
            go.Scatter(
                x=Hs,
                y=Ustars,
                mode="lines+markers",
                line=dict(color="crimson", width=3),
                marker=dict(size=8),
            ),
            row=1,
            col=1,
        )
        fig.update_xaxes(title_text="Number of humans (H)", row=1, col=1)
        fig.update_yaxes(title_text="Equilibrium backlog U*", row=1, col=1)

        fig.add_trace(
            go.Scatter(
                x=Hs,
                y=throughputs,
                mode="lines+markers",
                line=dict(color="forestgreen", width=3),
                marker=dict(size=8),
            ),
            row=1,
            col=2,
        )
        fig.update_xaxes(title_text="Number of humans (H)", row=1, col=2)
        fig.update_yaxes(title_text="Steady-state throughput (tokens/hr)", row=1, col=2)

        fig.update_layout(
            height=480, template="plotly_white", showlegend=False, hovermode="x unified"
        )
        return fig
