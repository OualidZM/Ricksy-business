import urllib.request
import pymongo
from bson.json_util import dumps
from pymongo.errors import ConnectionFailure
import dns


def get_page(page):  # llegir html
    try:
        pagee = urllib.request.urlopen(page)
        content = str(pagee.read())
        return content
    except:
        raise ValueError('error')


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


def target_dictionary(page):
    scrap_list = [scrapper_target(page)]
    if scrap_list:
        list = []
        start = 0
        end = 4
        elem = 0
        while len(list) < 9:
            list.append(scrap_list[0][start:end])
            if len(list[0]) != 0:
                start += 4
                end += 4
                nombre = list[elem][0]
                plazas = int(list[elem][1])
                alcance = list[elem][2]
                precio = list[elem][3]
                elem += 1
                nave = {'Nombre': nombre, 'Plazas': plazas,
                        'Alcance': alcance, 'Precio': precio}
                mongo(nave)
                print(nave)

            else:
                break


def mongo(nave):
    client = pymongo.MongoClient(
        "mongodb+srv://m001-student:123456789mongo@sandbox.gmy0y.mongodb.net/?retryWrites=true&w=majority")
    db = client.naves  # db
    collection_ovni = db.ofertas  # coll
    try:
        x = collection_ovni.insert_one(nave)
        return x
    except: 
        raise Exception('something went wrong')

    print(x + "There's your starhip!")



    # client = pymongo.MongoClient("mongodb+srv://m001-student:123456789mongo@sandbox.gmy0y.mongodb.net/?retryWrites=true&w=majority")
    # db = client.naves
    # col = db.test_ovni
    # return col.insert_one(nave)

if __name__ == "__main__":

    target_dictionary(
        'https://oualidzm.github.io/Ricksy-business/web/Index/Index_1.html')