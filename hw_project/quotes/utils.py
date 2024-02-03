from pymongo import MongoClient
import certifi


def get_mongodb():
    client = MongoClient(f"mongodb+srv://web_dz08:15061992@artem.z75si5r.mongodb.net/", tlsCAFile=certifi.where())

    db = client.HW_Web_10
    return db
