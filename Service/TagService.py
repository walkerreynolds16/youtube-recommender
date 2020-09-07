import Util.GeneralUtil as GeneralUtil

from pymongo import MongoClient

DBConnectionString = "mongodb+srv://api:LZnl6oHCbXK8Sp74@youtube-recommender-clu.ggqwr.mongodb.net/?retryWrites=true&w=majority"



def getYTTagFromDB(tagString):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Tag']

    res = None
    if(not tagString):
        res = sorted(list(collection.find({})), key=lambda tag: tag['tagString'])

    else:
        res = collection.find_one({'tagString': tagString})

    client.close()

    return res

def createYTTagInDB(tagString):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Tag']

    collection.insert_one({"tagString": tagString, "useCount": 0, "parentTopics": []})

    client.close()



def deleteYTTagFromDB(tagString):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Tag']

    collection.delete_one({"tagString": tagString})

    client.close()
