def get_next_target(content):

    start_link = content.find('<a href=')
    start_link = content.find('<a')

    if start_link == -1:
        return None, 0
    start_of_link = content.find('href=', start_link)
    start_quote = content.find('"', start_of_link)
    end_quote = content.find('"', start_quote + 1)
    url = content[start_quote + 1:end_quote]
    return url, end_quote
