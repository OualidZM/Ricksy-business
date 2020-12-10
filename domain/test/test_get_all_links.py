import pytest
from src.app import get_all_links
from src.app import get_page


def nice_list(content):
    assert(get_all_links(get_page('https://oualidzm.github.io/Ricksy-business/Projecta/Index/Index_1.html'))
           ) == ['https://oualidzm.git...dex_1.html', 'https://oualidzm.git...igera.html', 'https://oualidzm.git...diana.html', 'https://oualidzm.git...rande.html']
