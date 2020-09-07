import json
import Util.TopicUtil as TopicUtil
import Util.GeneralUtil as GeneralUtil


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


def getChannelTopics(youtube, channelIds):

    channelTopicMap = {}

    for chunk in GeneralUtil.chunkList(channelIds, 50):
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
    


def getUploadPlaylistId(youtube, channelId):
    request = youtube.channels().list(
            part="contentDetails",
            id=channelId
        )

    response = request.execute()

    print(json.dumps(response))

    if(len(response['items']) > 0):
        return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    else:
        return None


def getVideoIdsInPlaylist(youtube, playlistId):
    videoIds = []

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlistId,
        maxResults=50
    )

    response = request.execute()

    while(True):

        for item in response['items']:
            videoIds.append(item['contentDetails']['videoId'])

        if('nextPageToken' not in response):
            break

        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlistId,
            maxResults=50,
            pageToken=response['nextPageToken']
        )
        
        response = request.execute()

    return videoIds


def getTagsForListOfVideoIds(youtube, videoIds):
    videoTagData = {}

    for chunk in GeneralUtil.chunkList(videoIds, 50):
        idString = ""

        for videoId in chunk:
            idString += videoId + ','

        idString = idString[:-1]

        request = youtube.videos().list(
            part="snippet,topicDetails",
            id=idString
        )
        response = request.execute()
        
        for video in response['items']:
            tagData = {}
            
            if('tags' in video['snippet']):
                tagData['tags'] = video['snippet']['tags']
            if('topicDetails' in video):
                tagData['topicDetails'] = video['topicDetails']

            videoTagData[video['snippet']['title']] = tagData


    return videoTagData