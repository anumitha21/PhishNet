import os
import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

uri = os.getenv("MONGO_DB_URL") or os.getenv("MONGODB_URL_KEY")

if not uri:
    print("Error: MONGO_DB_URL is not set in your .env file.")
    print("Please set MONGO_DB_URL in your .env file with your MongoDB connection string.")
    exit(1)

ca = certifi.where()

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
