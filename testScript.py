
import os
import json

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client import client # Added
from oauth2client import tools # Added
from oauth2client.file import Storage # Added

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_authenticated_service(): # Modified
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret.json"

    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secrets_file, scopes)
        credentials = tools.run_flow(flow, store)
    return googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

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
    



def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    
    youtube = get_authenticated_service()
    
    channelIds = getSubscriptions(youtube)

    channelTopicMap = getSubscriptionTopics(youtube, channelIds)

    uniqueTopics = {}
    for channel in channelTopicMap.keys():
        topicList = channelTopicMap[channel]

        for topic in topicList:
            if(topic in uniqueTopics):
                uniqueTopics[topic].append(channel)
            else:
                uniqueTopics[topic] = [channel]

    print(json.dumps(uniqueTopics))


if __name__ == "__main__":
    main()