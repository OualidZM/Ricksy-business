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
    start_link = content.find('<a')
    if start_link == -1:
        return None, 0
    start_of_link = content.find('href=', start_link)
    start_quote = content.find('"', start_of_link)
    end_quote = content.find('"', start_quote + 1)
    url = content[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(content):
    links = []
    while True:
        url, endpos = get_next_target(content)
        if url:
            if url[0:7] == 'https://':
                links.append(url)
                content = content[endpos:]
            else:
                links.append(
                    'https://oualidzm.github.io/Ricksy-business/web'+url[2:])
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


def scrapper(page):  # page==link original
    # crida al crawler i agafa la llista de links // page==link original
    to_scrap = crawl_web(page)
    scrap_target = []  # datos que interesan
    while to_scrap:  # 'mentres hi hagi links a to_scrap...'
        page = to_scrap.pop()  # agafa s'ultim link de to_scrap (desapareix de to_scrap)//cambiam variable page. page == to_scrap.pop() (ultim link de la llista "to_scrap")
        # converteix es link de page en un document que se pot llegir//page==ultim link de la llista "to_scrap"
        target = get_page(page)
        initial_mark = target.find('id="text-align-')
        if initial_mark != -1:
            scrap_target.append(page)
        else:
            continue
    for i in scrap_target:
        target = get_page(i)

        # start_data = target.find(':', initial_mark)
        # end_data = target.find('<', start_data)
        # data = target[start_data + 1:end_data]
        # scrap_target.append(data)
        # initial_mark = start_data+1


if __name__ == "__main__":

    # get_page('https://oualidzm.github.io/Ricksy-business/Projecta/Index/Index_1.html')
    # get_next_target(content)
    # get_all_links(content)
    scrapper(
        'https://oualidzm.github.io/Ricksy-business/web/Index/Index_1.html')
