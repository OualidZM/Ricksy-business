import urllib.request


def get_page(page):  # llegir html
    try:
        pagee = urllib.request.urlopen(page)
        content = str(pagee.read())
        return content
    except:
        raise ValueError('error')
