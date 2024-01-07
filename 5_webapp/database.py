import pymongo
from settings import DATABASE

client = pymongo.MongoClient(DATABASE['host'], DATABASE['port'])
db = client[DATABASE['name']]
