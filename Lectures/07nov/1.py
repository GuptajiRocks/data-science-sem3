from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://e23cseu0055:cKHGCHeluZY7iYmq@trialone.ghqx2.mongodb.net/?retryWrites=true&w=majority&appName=trialone"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

database = client["trialonee"]
print(database)