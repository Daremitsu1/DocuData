import os
import pymysql
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# ---------------------- MySQL Connection ----------------------
def get_db_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )

# ---------------------- MongoDB Connection ----------------------
def get_mongo_connection():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("MONGO_DB")]
    return db[os.getenv("MONGO_COLLECTION")]
