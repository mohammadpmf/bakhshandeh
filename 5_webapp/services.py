from bson import ObjectId
from database import db
from scrape import fetch_xml, NAMESPACE


def news_list() -> list:
    cursor = db.news.find()
    data = []
    for document in cursor:
        document['_id'] = str(document['_id'])
        data.append(document)
    return data


def news_details(object_id: str):
    cursor = db.news.find({"_id": ObjectId(object_id)})
    if not len(list(cursor.__copy__())):
        msg = {'message': 'News does not exist.'}
        return msg
    for document in cursor:
        print(document)
        document['_id'] = str(document['_id'])
    return document


def news_search(query:str) -> list:
    q = {
        "$or": [
            {"title": {"$regex": query, "$options": "i"}},
            {"description": {"$regex": query, "$options": "i"}}
        ]
    }
    
    cursor = db.news.find(q)
    data = []
    for document in cursor:
        document['_id'] = str(document['_id'])
        data.append(document)
    return data


def news_create(obj: dict):
    db.news.insert_one(obj)


def news_exist(title: str) -> bool:
    if len(list(db.news.find({"title": title}))):
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
             "creator": item.find('dc:creator', NAMESPACE).text,
             "pubDate": item.find('pubDate').text,
        }
        news_create(obj)
    msg = {'message': 'Update successfully done.'}
    return msg
