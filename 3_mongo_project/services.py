import requests
import xml.etree.ElementTree as ET
import pymongo


def fetch_xml():
    response = requests.get("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    xml_tree = ET.fromstring(response.content)
    return xml_tree.findall('.//item')


def news_search(query:str) -> list:
    q = {
        "$or": [
            {"title": {"$regex": query, "$options": "i"}},
            {"description": {"$regex": query, "$options": "i"}}
        ]
    }
    cursor = coll.find(q)
    data = []
    for document in cursor:
        document['_id'] = str(document['_id'])
        data.append(document)
    return data


def news_exist(title: str) -> bool:
    if len(list(coll.find({"title": title}))):
        return True
    else:
        return False
    

def update_collection():
    try:
        items = fetch_xml()
    except:
        msg = {'message': 'Try again.'}
        return msg
    for item in items:
        title = item.find('title').text
        if news_exist(title):
            continue
        obj = {
            "title": title,
            "description": item.find('description').text,
            "link": item.find('link').text,
            "creator": item.find('dc:creator', {'dc': 'http://purl.org/dc/elements/1.1/'}).text,
            "pubDate": item.find('pubDate').text,
        }
        coll.insert_one(obj)
    msg = {'message': 'Update successfully done.'}
    return msg


client = pymongo.MongoClient('localhost', 27017)
db = client.get_database('feeds')
coll = db.get_collection('news')
