import eventlet
eventlet.monkey_patch()

import requests
from flask import Flask
import json


def setup(app, args):
    app.run()

def createFlaskApp():
    # Set up app object
    app = Flask(__name__)

    # Setup some configs for the flask app
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.secret_key = "secretKey!@#$"

    # Setup blueprints
    # Don't know why, but these imports have to be right before registering the blueprint
    # It doesn't work otherwise, ¯\_(ツ)_/¯
    # from APIs.ProfileAPI import profileBP
    # from APIs.LobbyAPI import lobbyBP
    # from APIs.LoginAPI import loginBP
    # from APIs.PlaylistAPI import playlistBP
    # from APIs.TestingAPI import testingBP

    # app.register_blueprint(profileBP, url_prefix="/profile")
    # app.register_blueprint(lobbyBP, url_prefix="/lobby")
    # app.register_blueprint(loginBP, url_prefix="/login")
    # app.register_blueprint(playlistBP, url_prefix="/playlist")
    # app.register_blueprint(testingBP, url_prefix="/testing")


    from Resource.TopicResource import topicBP

    app.register_blueprint(topicBP, url_prefix="/topic")
    
    return app
