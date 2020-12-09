from pymongo import pymongo
import dns
from bson.json_util import dumps
from pymongo.errors import ConnectionFailure


def mongo_dict(nave):
    client = pymongo.MongoClient(
        "mongodb+srv://m001-student:123456789mongo@sandbox.gmy0y.mongodb.net/?retryWrites=true&w=majority")
    db = client.naves  # db
    collection_ovni = db.ofertas  # coll
    x = collection_ovni.insert_one(nave)
    return x
