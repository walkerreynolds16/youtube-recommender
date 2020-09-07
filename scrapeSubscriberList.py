import Service.ChannelService as ChannelService
import Util.GeneralUtil as GeneralUtil
import Util.YouTubeManager as YouTubeManager
import json


channelIds = []
with open("./Scripts/files/subscriberList.htm") as inFile:
    for line in inFile.readlines():
        if("/youtube/channel/" in line):
            startIndex = line.index("/youtube/channel/")
            endIndex = line.index("\"", startIndex)

            channelId = line[startIndex + len("/youtube/channel/"):endIndex]
            channelIds.append(channelId)

            # if len(channelIds) == 50:
            #     break


youtube = YouTubeManager.get_authenticated_service()

channelMap = ChannelService.getChannelData(youtube, channelIds, "snippet,topicDetails")


insertData = []
print(len(channelMap.keys()))
for channelId in channelMap.keys():
    channelData = channelMap[channelId]

    temp = {}
    temp['url'] = "https://www.youtube.com/channel/{}".format(channelId)
    temp['title'] = channelData['snippet']['title']
    temp['tags'] = []
    temp['channelId'] = channelId


    if('description' in channelData['snippet']):
        temp['description'] = channelData['snippet']['description']

    if("thumbnails" in channelData['snippet']):
        temp['thumbnail'] = channelData['snippet']['thumbnails']['default']['url']

    if("topicDetails" in channelData and 'topicCategories' in channelData['topicDetails']):
        temp['topics'] = channelData['topicDetails']['topicCategories']

    insertData.append(temp)


# print(json.dumps(insertData))

with open("testInsertData.json", "w") as outputFile:
    outputFile.write(json.dumps(insertData))

