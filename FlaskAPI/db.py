from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    client = MongoClient(os.getenv('MONGO_URI'))
    return client.inventory_management

def inventory_data():
    client = MongoClient(os.getenv('MONGO_URI'))
    return client.inventory_data

def product_data():
    client = MongoClient(os.getenv('MONGO_URI'))
    return client.product_data

def supplier_data():
    client = MongoClient(os.getenv('MONGO_URI'))
    return client.supplier_data

def sale_data():
    client = MongoClient(os.getenv('MONGO_URI'))
    return client.sale_data