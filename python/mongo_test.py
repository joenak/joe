from pymongo import MongoClient

from pprint import pprint
x = 1
while x < 10:
    client = MongoClient("mongodb://172.16.248.100:27017/?replicaSet=mongo_j")
    db = client.joe
    collection = db.test1
    j = collection.find_one({'name':'joe'})
    pprint(j)    
