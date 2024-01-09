import requests
import pymongo

def get_info():
    information = requests.get("https://one-api.ir/rss/?token=387675:647ef9c69284b&action=varzesh3").json()
    result = information['result']
    items = result.get("item")
    return items    

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
        items = get_info()
    except:
        msg = {'message': 'Try again.'}
        return msg
    for item in items:
        title = item.get("title")
        if news_exist(title):
            continue
        link = item.get("link")
        description = item.get("description")
        pubDate = item.get("pubDate")
        date = pubDate[0:pubDate.index('T')]
        time = pubDate[pubDate.index('T')+1:]
        obj = {
            "title": title,
            "link": link,
            "description": description,
            "date": date,
            "time": time,
        }
        coll.insert_one(obj)
    msg = {'message': 'Update successfully done.'}
    return msg


client = pymongo.MongoClient('localhost', 27017)
db = client.get_database('iran')
coll = db.get_collection('varzesh3')
