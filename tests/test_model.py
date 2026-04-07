import numpy as np

from ai_human_token_model import AIHumanTokenModel


def test_rate_decreases_as_backlog_increases():
    model = AIHumanTokenModel()
    low_backlog_rate = model.rate(0.0)
    high_backlog_rate = model.rate(20_000.0)
    assert high_backlog_rate < low_backlog_rate


def test_simulate_discrete_euler_has_expected_shape_and_non_negative_values():
    model = AIHumanTokenModel()
    t, u = model.simulate_discrete_euler(U0=200.0, steps=25, dt=0.5)
    assert len(t) == 25
    assert len(u) == 25
    assert np.isclose(u[0], 200.0)
    assert np.all(u >= 0.0)


def test_simulate_discrete_map_has_expected_shape_and_non_negative_values():
    model = AIHumanTokenModel()
    t, u = model.simulate_discrete_map(U0=200.0, steps=25)
    assert len(t) == 25
    assert len(u) == 25
    assert np.isclose(u[0], 200.0)
    assert np.all(u >= 0.0)


def test_equilibrium_is_non_negative_and_near_stationary():
    model = AIHumanTokenModel()
    u_star, throughput = model.get_equilibrium()
    assert u_star >= 0.0
    assert throughput >= 0.0
    assert abs(model.rate(u_star)) < 1e-4
