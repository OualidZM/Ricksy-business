from ..src.crawler import get_next_target
import pytest

def get_next_target(content):
    assert(get_next_target(content)), ('../sel_nav/sel_nav.html', 640))