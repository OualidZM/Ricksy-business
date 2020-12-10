from src.app import crawl_web
import pytest



def correct():
    assert crawl_web("https://oualidzm.github.io/Ricksy-business/web/Index/Index_1.html") == ['https://oualidzm.git...dex_1.html', 'https://oualidzm.git...l_nav.html', 'https://oualidzm.git...rande.html', 'https://oualidzm.git...serva.html', 'https://oualidzm.git...izada.html', 'https://oualidzm.git...diana.html', 'https://oualidzm.git...igera.html']






