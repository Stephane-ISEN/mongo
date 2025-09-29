from pymongo import MongoClient
from dto.config import MDB_CONNECTION, MDB_BASE, MDB_COLLECTION
from bson import ObjectId

class Connexion:

    @classmethod
    def connect(cls):
        cls.client = MongoClient(MDB_CONNECTION)
        cls.db = cls.client[MDB_BASE]
        cls.collection = cls.db[MDB_COLLECTION]
    
    @classmethod
    def get_all_fruits(cls):
        return cls.collection.find()
    
    @classmethod
    def get_fruit_by_id(cls, fruit_id):
        return cls.collection.find_one({"_id": ObjectId(fruit_id)})
    
    @classmethod
    def add_fruit(cls, fruit_data):
        return cls.collection.insert_one(fruit_data).inserted_id
    
    @classmethod
    def update_fruit(cls, fruit_id, update_data):
        cls.collection.update_one({"_id": ObjectId(fruit_id)}, {"$set": update_data})

    @classmethod
    def delete_fruit(cls, fruit_id):
        cls.collection.delete_one({"_id": ObjectId(fruit_id)})

    @classmethod
    def disconnect(cls):
        cls.client.close()

