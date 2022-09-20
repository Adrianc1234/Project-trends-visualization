"""
#mongodb+srv://general:General2022..@cluster0.mfzpwpz.mongodb.net/?retryWrites=true&w=majority

import pymongo

from pymongo import MongoClient
myclient = MongoClient("mongodb+srv://general:General2022..@cluster0.mfzpwpz.mongodb.net/?retryWrites=true&w=majority")

# Calling the database from the cluster
db = myclient["IGinstagram"]
collection = db["scrapers"]

# Sample data to add in the collection
post1 = {"_id": 0, "name": "Karatsi","score":3, "age":21}

collection.insert_one(post1)

"""
import os
os.system("python3 preprocessing.py")