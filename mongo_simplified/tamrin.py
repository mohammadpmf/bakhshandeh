import pymongo

from laptops import *

client = pymongo.MongoClient("localhost", 27017)
db = client.get_database('shop')

coll = db.get_collection('laptops')
# coll.insert_many(laptops)
data = coll.find()
for item in data:
    print(f"Brand: {item['brand']:<10} Price: {item['price']:<10} CPU: {item['cpu']:<5} RAM: {item['ram']:<3}")

# coll.find_one_and_delete({'brand': 'apple'})
# coll.find_one_and_update({'brand': 'apple'}, {"$set":laptop4}, upsert=True)
