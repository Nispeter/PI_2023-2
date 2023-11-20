from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://jeesus1423:1234567j@cluster0.oirouk8.mongodb.net/?retryWrites=true&w=majority&ssl=true"
# Create a new client and connect to the server
con = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    con.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)