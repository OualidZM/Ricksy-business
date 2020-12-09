from src.app import union
import pytest


@pytest.mark.p_False_q_True
def union(p, q):
    assert(union(p, q([], [1,2,3])), [1,2,3], [1,2,3])

@pytest.mark.p_y_q_False
def union(p, q):
    assert(get_all_links(get_page([],[])), [],[])

@pytest.mark.p_menor_q
def union(p, q):
    assert(get_all_links(get_page([2,3],[1,3,4])), [1,2,3,4],[1,3,4])