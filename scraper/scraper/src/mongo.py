import pymongo
from bson.json_util import dumps
from pymongo.errors import ConnectionFailure
import dns




client = pymongo.MongoClient("mongodb+srv://m001-student:123456789mongo@sandbox.gmy0y.mongodb.net/?retryWrites=true&w=majority")
db = client.test_ovni_bien
col = db.test_ovni
x= col.insert_one({"test":"ess","test2":5})
print(x) 
