from flask import Flask, request, jsonify, json, Blueprint, session
from Util.JSONEncoder import JSONEncoder
import Util.YouTubeManager as YouTubeManager
import Service.ChannelService as ChannelService

import json

channelBP = Blueprint("channel", __name__)

youtube = YouTubeManager.get_authenticated_service()


@channelBP.route("/youtube", methods=['GET'])
def getYoutubeChannel():
    channelId = request.args.get('id')

    if(not channelId):
        return "No id provided"

    channel = ChannelService.getYTChannelFromDB(channelId)

    return JSONEncoder().encode(channel)

@channelBP.route("/youtube", methods=['POST'])
def createYoutubeChannel():
    requiredFields = ['url', 'title', 'tags', 'channelId', 'description', 'thumbnail', 'topics']
    print(request.get_json())
    for field in requiredFields:
        if field not in request.get_json():
            return "A required field was not provided"

    # if(field not in request.get_json() for field in requiredFields):
    #     return "A required field was not provided"
    
    channel = ChannelService.createYTChannelInDB(request.get_json())

    return JSONEncoder().encode(channel)


@channelBP.route("/youtube", methods=['PUT'])
def updateYoutubeChannel():
    channelId = request.json.get('channelId')
    tags = request.json.get('tags')


    ChannelService.updateYTChannelInDB(channelId, tags)

    return '', 204

@channelBP.route("/youtube", methods=['DELETE'])
def deleteYoutubeChannel():
    channelId = request.json.get("channelId")
    print(channelId)
    if(not channelId):
        return "ChannelId was not provided"

    ChannelService.deleteYTChannelFromDB(channelId)

    return '', 200


@channelBP.route("/youtube/random", methods=['GET'])
def getRandomYoutubeChannel():
    noTags = request.args.get('noTags')

    channel = ChannelService.getRandomYTChannelFromDB(noTags)

    return JSONEncoder().encode(channel)