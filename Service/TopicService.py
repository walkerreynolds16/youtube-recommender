import json


def getSubscriptions(youtube):
    channelIds = []
    finished = False

    request = youtube.subscriptions().list(
            part="snippet,contentDetails",
            mine=True,
            maxResults=50,
        )

    response = request.execute()

    while(not finished):
        for item in response['items']:
            channelIds.append(item['snippet']['resourceId']['channelId'])

        if('nextPageToken' not in response):
            finished=True
            break

        request = youtube.subscriptions().list(
            part="snippet,contentDetails",
            mine=True,
            maxResults=50,
            pageToken=response['nextPageToken']
        )
        
        response = request.execute()

    return channelIds

def chunkChannelIds(channelIds, size):
    for i in range(0, len(channelIds), size):
        yield channelIds[i:i + size]

def getSubscriptionTopics(youtube, channelIds):

    channelTopicMap = {}

    for chunk in chunkChannelIds(channelIds, 50):
        idString = ""
        for id in chunk:
            idString += id + ","

        idString = idString[:-1]
        request = youtube.channels().list(
            part="snippet,topicDetails",
            id=idString
        )

        response = request.execute()

        for item in response['items']:
            channelTopicMap[item['snippet']['title']] = item['topicDetails']['topicCategories']

    return channelTopicMap
    
