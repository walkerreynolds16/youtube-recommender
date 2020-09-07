from flask import Flask, request, jsonify, json, Blueprint, session
from Util.JSONEncoder import JSONEncoder
import Util.YouTubeManager as YouTubeManager
import Service.TopicService as TopicService
import Util.TopicUtil as TopicUtil

import json

topicBP = Blueprint("topic", __name__)

youtube = YouTubeManager.get_authenticated_service()


@topicBP.route("/channels", methods=['GET'])
def getTopicsForChannels():
    channelIds = TopicService.getSubscriptions(youtube)

    channelTopicMap = TopicService.getChannelTopics(youtube, channelIds)

    return json.dumps(channelTopicMap)


@topicBP.route("/unique", methods=['GET'])
def getChannelsForTopics():
    channelIds = TopicService.getSubscriptions(youtube)

    channelTopicMap = TopicService.getChannelTopics(youtube, channelIds)

    uniqueTopics = TopicUtil.flipChannelTopicMap(channelTopicMap)
    
    return json.dumps(uniqueTopics)


'''
    to find all videos, first get channel id -> get uploads playlist id -> get video ids in playlist -> find tags for each video id

'''
@topicBP.route("/videoTags", methods=['GET'])
def getVideoTags():
    videoTags = {}
    
    # DON'T CHANGE CHANNEL ID!!! 
    # IF CHANNEL HAS LOTS OF VIDS, SAY BYE BYE TO OUR API QUOTA
    channelId = "UCtqxG9IrHFU_ID1khGvx9sA"

    uploadPlaylistId = TopicService.getUploadPlaylistId(youtube, channelId)

    if(uploadPlaylistId):
        videoIds = TopicService.getVideoIdsInPlaylist(youtube, uploadPlaylistId)

        videoTagData = TopicService.getTagsForListOfVideoIds(youtube, videoIds)

    return json.dumps(videoTagData)
