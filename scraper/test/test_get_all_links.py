from src.crawler import get_all_links
import pytest


def get_all_links(content):
    assert(get_all_links(get_page('https://oualidzm.github.io/Ricksy-business/Projecta/Index/Index_1.html'))) == [../sel_nav/sel_nav.html]
    assert(get_all_links(get_page('https://oualidzm.github.io/Ricksy-business/Projecta/sel_nav/sel_nav.html'))) == [../Index/Index_1.html, ]
