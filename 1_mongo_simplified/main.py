import pymongo
from bson import ObjectId

from data import news_data

client = pymongo.MongoClient("localhost", 27017)
db = client.get_database('feeds')

# # command #0
# print(db)

# # command #1
# data = db.list_collection_names()
# print(data)

# # command #2
# news = db.get_collection('news')
# print(news)

# # command #3
# # Insert One
# db['news'].insert_one(khabar)
# data = db['news'].find()
# for news in data:
#    print('-'*50, end='\n'*3)
#    print(news)
#    print('-'*80, end='\n'*3)

# # command #4
# # Insert Many
# db['news'].insert_many(news_data)
# data = db['news'].find()
# for news in data:
#     print('-'*50, end='\n'*3)
#     print(news)
#     print('-'*80, end='\n'*3)


# # command #5
# # Read
# data = db['news'].find()
# for news in data:
#     print('-'*50, end='\n'*3)
#     print(news)
#     print('-'*80, end='\n'*3)


# # command #6
# # Read and show specific columns
# data = db['news'].find({}, {"_id":0, "link": 1, 'creator':1})
# print('-'*80)
# for news in data:
#     print(news)
#     print('-'*80)


# # command #7
# # Read with query
# data = db['news'].find_one({"creator": "Christopher F. Schuetze"}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')
# data = db['news'].find_one({"creator": {'$regex': 'Emma'}}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')
# data = db['news'].find_one({"_id": ObjectId("65916a63532af8c98b973c69")}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')


# # command #8
# # Update document
# data = db['news'].find_one({"_id": ObjectId("65916a63532af8c98b973c69")}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')
# result = db['news'].update_one({"_id": ObjectId('65916a63532af8c98b973c69')}, {"$set": {"title": "New Thing 4"}})
# print(result.upserted_id)
# data = db['news'].find_one({"_id": ObjectId("65916a63532af8c98b973c69")}, { "_id": 1, 'title':1})
# print(data['title'], end='\n'+50*'-'+'\n')

# # command #9
# # Delete document
# db['news'].delete_one({"_id": ObjectId('6523cea567011e412a93a3a1')})
