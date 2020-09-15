from flask import Flask, request, jsonify, json, Blueprint, session
from Util.JSONEncoder import JSONEncoder
import Util.YouTubeManager as YouTubeManager
import Service.TagService as TagService

import json

tagBP = Blueprint("tag", __name__)

youtube = YouTubeManager.get_authenticated_service()


@tagBP.route("/youtube", methods=['GET'])
def getYoutubeTag():
    tagString = request.args.get('tagString')

    # if(not tagString):
    #     return "No tag provided"

    tag = TagService.getYTTagFromDB(tagString)

    return JSONEncoder().encode(tag)

@tagBP.route("/youtube", methods=['POST'])
def createYoutubeTag():
    tagString = request.json.get('tagString')
    category = request.json.get('category')

    TagService.createYTTagInDB(tagString, category)

    return '', 204

@tagBP.route("/youtube", methods=['PUT'])
def updateYoutubeTag():
    pass

@tagBP.route("/youtube", methods=['DELETE'])
def deleteYoutubeTag():
    tagString = request.json.get('tagString')

    if(not tagString):
        return "No tagString provided"

    TagService.deleteYTTagFromDB(tagString)

    return '', 204

