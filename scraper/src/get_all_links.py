from get_next_target import get_next_target


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
