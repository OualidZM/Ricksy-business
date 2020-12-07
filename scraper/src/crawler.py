import urllib.request

def get_page(page):  # llegir html
    try:
        pagee = urllib.request.urlopen(page)
        content = str(pagee.read())
    except:
        raise ValueError('error')
    return content

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

if __name__ == "__main__":

    get_page('https://oualidzm.github.io/Ricksy-business/Projecta/Index/Index_1.html')