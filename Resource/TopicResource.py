from flask import Flask, request, jsonify, json, Blueprint, session
from Util.JSONEncoder import JSONEncoder
import Util.YouTubeManager as YouTubeManager
import Service.TopicService as TopicService

topicBP = Blueprint("topic", __name__)


@topicBP.route("/test", methods=['GET'])
def testTopic():
    print("reee")

    youtube = YouTubeManager.get_authenticated_service()

    channelIds = TopicService.getSubscriptions(youtube)

    channelTopicMap = TopicService.getSubscriptionTopics(youtube, channelIds)

    uniqueTopics = {}
    for channel in channelTopicMap.keys():
        topicList = channelTopicMap[channel]

        for topic in topicList:
            if(topic in uniqueTopics):
                uniqueTopics[topic].append(channel)
            else:
                uniqueTopics[topic] = [channel]

    

    return json.dumps(uniqueTopics)