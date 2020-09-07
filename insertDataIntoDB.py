from pymongo import MongoClient

DBConnectionString = "mongodb+srv://api:LZnl6oHCbXK8Sp74@youtube-recommender-clu.ggqwr.mongodb.net/?retryWrites=true&w=majority"




client = MongoClient(DBConnectionString)
db = client.YT_Recommender

collection = db['YT_Channel']

res = collection.find({})

for item in res:
    print(item)

