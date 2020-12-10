from services.app import union
import pytest


@pytest.mark.p_False_q_True
def test_no_p():
    assert union([], [1, 2, 3]) == [1, 2, 3]


@pytest.mark.p_y_q_False
def p_n_q():
    assert union([], []) == []


@pytest.mark.p_menor_q
def p_menor_q():
    assert union([2, 3], [1, 3, 4]) == [1, 2, 3, 4]
