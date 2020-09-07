import Util.GeneralUtil as GeneralUtil

from pymongo import MongoClient

DBConnectionString = "mongodb+srv://api:LZnl6oHCbXK8Sp74@youtube-recommender-clu.ggqwr.mongodb.net/?retryWrites=true&w=majority"


def getChannelData(youtube, channelIds, part):

    channelMap = {}

    for chunk in GeneralUtil.chunkList(channelIds, 50):
        idString = ""
        for id in chunk:
            idString += id + ","

        idString = idString[:-1]
        request = youtube.channels().list(
            part=part,
            id=idString
        )

        response = request.execute()

        for item in response['items']:
            channelMap[item['id']] = item

    return channelMap
    

def getYTChannelFromDB(channelId):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Channel']

    channel = collection.find_one({'channelId': channelId})
    client.close()


    return channel

def updateYTChannelInDB(channelId, tags):
    client = MongoClient(DBConnectionString)
    db = client.YT_Recommender
    collection = db['YT_Channel']

    collection.update_one({'channelId': channelId}, {'$set': {"tags": tags}})

    client.close()
