from .crawl_web import crawl_web
from .get_page import get_page


def scrapper_target(page):  # page==link original
    # crida al crawler i agafa la llista de links // page==link original
    to_scrap = crawl_web(page)
    scrap_target = []  # datos que interesan(pagines de ses naus)
    while to_scrap:  # 'mentres hi hagi links a to_scrap...'
        page = to_scrap.pop()  # agafa s'ultim link de to_scrap (desapareix de to_scrap)//cambiam variable page. page == to_scrap.pop() (ultim link de la llista "to_scrap")
        # converteix es link de page en un document que se pot llegir//page==ultim link de la llista "to_scrap"
        target = get_page(page)
        initial_mark = target.find('id="text-align-')
        count = 0
        while initial_mark != -1:
            if count <= 11:
                # target = scrapper_target(get_page(page))
                start_data = target.find(':', initial_mark)
                end_data = target.find('<', start_data)
                data = target[start_data + 1:end_data]
                scrap_target.append(data)
                initial_mark = start_data+1
                count += 1
            else:
                break
        else:
            continue
    return scrap_target
