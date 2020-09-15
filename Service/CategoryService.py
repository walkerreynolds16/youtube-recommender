import Util.GeneralUtil as GeneralUtil

from pymongo import MongoClient

DBConnectionString = "mongodb+srv://api:LZnl6oHCbXK8Sp74@youtube-recommender-clu.ggqwr.mongodb.net/?retryWrites=true&w=majority"


def getYTCategoryFromDB(category):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Category']

    res = None
    if(not category):
        res = sorted(list(collection.find({})), key=lambda category: category['category'])

    else:
        res = collection.find_one({'category': category})

    client.close()

    return res

def createYTCategoryInDB(category):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Category']

    collection.insert_one({"category": category, "subTags": 0})

    client.close()



def deleteYTCategoryFromDB(category):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Category']

    collection.delete_one({"category": category})

    client.close()
