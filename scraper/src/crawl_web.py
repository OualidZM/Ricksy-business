from .get_all_links import get_all_links
from .get_page import get_page
from .union import union


def crawl_web(page):
    tocrawl = [page]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
        else:
            continue
    return crawled
