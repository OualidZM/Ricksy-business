from src.app import union
import pytest



def test_no_p():
    assert union([], [1, 2, 3]) == [1, 2, 3]



def p_n_q():
    assert union([], []) == []




def p_menor_q():
    assert union([2, 3], [1, 3, 4]) == [1, 2, 3, 4]
