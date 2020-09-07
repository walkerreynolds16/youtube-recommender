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
    pass

@channelBP.route("/youtube", methods=['PUT'])
def updateYoutubeChannel():
    channelId = request.json.get('channelId')
    tags = request.json.get('tags')


    ChannelService.updateYTChannelInDB(channelId, tags)

    return '', 204

@channelBP.route("/youtube", methods=['DELETE'])
def deleteYoutubeChannel():
    pass

