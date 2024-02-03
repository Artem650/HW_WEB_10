import json
import certifi
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient(f"mongodb+srv://web_dz08:15061992@artem.z75si5r.mongodb.net", tlsCAFile=certifi.where())

db = client.HW_Web_10

with open("quotes.json", "r", encoding="utf-8") as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({"fullname": quote["author"]})
    if author:
        db.quotes.insert_one({
            "quote": quote["quote"],
            "tags": quote["tags"],
            "author": ObjectId(author["_id"])
        })