from services.app import get_next_target
import pytest


def first_objective(content):
    assert(get_next_target(content)) == ('../sel_nav/sel_nav.html', 640)
