import pymongo
from pymongo.database import Database
from pymongo.collection import Collection


def get_db(databse:str) -> Database:
    client = pymongo.MongoClient("localhost", 27017)
    return client[databse]


def list_colecctions(databse:str) -> list:
    db = get_db(databse)
    return db.list_collection_names()


def get_collection(databse:str, collection:str) -> Collection:
    db = get_db(databse)
    return db.get_collection(collection)


def read(db:Database, collection:str, *args):
    return db[collection].find(*args)


def read_one(db:Database, collection:str, *args):
    return db[collection].find_one(*args)


def insert_one(db:Database, collection:str, data:dict):
    db[collection].insert_one(data)


def insert_many(db:Database, collection:str, data:dict):
    db[collection].insert_many(data)


def update(db:Database, collection:str, filter, *args):
    db[collection].update_one(filter, *args) 


def delete(db:Database, collection:str, filter):
    db[collection].delete_one(filter) 
