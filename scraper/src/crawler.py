import urllib.request

#content = ''


def get_page(page):  # llegir html
    try:
        pagee = urllib.request.urlopen(page)
        content = str(pagee.read())
        return content
    except:
        raise ValueError('error')


def get_next_target(content):
    start_link = content.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = content.find('"', start_link)
    end_quote = content.find('"', start_quote + 1)
    url = content[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(content):
    links = []
    while True:
        url, endpos = get_next_target(content)
        if url:
            if url[0:8] == 'https://':
                links.append(url)
                content = content[endpos:]
            else:
                links.append('https://'+url)
                content = content[endpos:]

        else:
            break
    return links


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


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


if __name__ == "__main__":

    # get_page('https://oualidzm.github.io/Ricksy-business/Projecta/Index/Index_1.html')
    # get_next_target(content)
    # get_all_links(content)
    crawl_web(
        'https://oualidzm.github.io/Ricksy-business/Projecta/Index/Index_1.html')
