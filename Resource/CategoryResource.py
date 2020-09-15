from flask import Flask, request, jsonify, json, Blueprint, session
from Util.JSONEncoder import JSONEncoder
import Util.YouTubeManager as YouTubeManager
import Service.CategoryService as CategoryService

import json

categoryBP = Blueprint("category", __name__)

youtube = YouTubeManager.get_authenticated_service()


@categoryBP.route("/youtube", methods=['GET'])
def getYoutubeCategory():
    category = request.args.get('category')

    category = CategoryService.getYTCategoryFromDB(category)

    if(not category):
        category = {}

    return JSONEncoder().encode(category)

@categoryBP.route("/youtube", methods=['POST'])
def createYoutubeCategory():
    category = request.json.get('category')

    CategoryService.createYTCategoryInDB(category)

    return '', 204

@categoryBP.route("/youtube", methods=['PUT'])
def updateYoutubeCategory():
    pass

@categoryBP.route("/youtube", methods=['DELETE'])
def deleteYoutubeCategory():
    category = request.json.get('category')

    if(not category):
        return "No category provided"

    CategoryService.deleteYTCategoryFromDB(category)

    return '', 204

