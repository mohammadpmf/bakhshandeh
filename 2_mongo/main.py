from bson import ObjectId
from bson.objectid import ObjectId

from mongos import get_db, list_colecctions, get_collection, read, read_one, insert_one, insert_many, update, delete
from data import news_data

db = get_db('feeds')

# command #0
print(db)


# # command #1
# # List Collections
# data = list_colecctions('feeds')
# print(data)


# # command #2
# # get_collection
# news = get_collection('feeds', 'news')
# print(news)


# # command #3# # Insert One
# news = {
#         "title": "Pope Benedict Lies In State, Drawing Thousands of Mourners",
#         "link":"https://www.nytimes.com/2023/01/02/world/europe/pope-benedict-lying-in-state.html",
#         "description": "The pope emeritus is lying in state in St. Peter`s Basilica, where some 65,000 mourners, including Roman Catholic faithful and tourists, had paid last respects by Monday evening.",
#         "creator":"Emma Bubola and Elisabetta Povoledo",
#         "pubDate":"Mon, 02 Jan 2023 18:28:22 +0000"
#     }
# insert_one(db, 'news', news)
# data = read(db, 'news')
# for news in data:
#    print('-'*50, end='\n'*3)
#    print(news)
#    print('-'*80, end='\n'*3)


# # command #4
# # Insert Many
# insert_many(db, 'news', news_data)
# data = read(db, 'news')
# for news in data:
#     print('-'*50, end='\n'*3)
#     print(news)
#     print('-'*80, end='\n'*3)


# # command #5
# # Read
# data = read(db, 'news')
# for news in data:
#     print('-'*50, end='\n'*3)
#     print(news)
#     print('-'*80, end='\n'*3)


# # command #6
# # Read and show specific columns
# data = read(db, 'news', {}, { "_id": 1, 'creator':1})
# print('-'*80)
# for news in data:
#     print(news)
#     print('-'*80)


# # command #7
# # Read with query
# data = read_one(db, 'news', {"_id": ObjectId("6523cea567011e412a93a3a1")}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')
# data = read_one(db, 'news', {"creator": "Christopher F. Schuetze"}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')
# data = read_one(db, 'news', {"creator": {'$regex': 'Emma'}}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')


# # command #8
# # Update document
# data = read_one(db, 'news', {"_id": ObjectId("6523cea567011e412a93a39e")}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')
# data = update(db, 'news', {"_id": ObjectId('6523cea567011e412a93a39e')}, {"$set": {"title": "New Thing"}})
# data = read_one(db, 'news', {"_id": ObjectId("6523cea567011e412a93a39e")}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')


# # command #9
# # Delete document
# data = delete(db, 'news', {"_id": ObjectId('6523cea567011e412a93a3a1')})