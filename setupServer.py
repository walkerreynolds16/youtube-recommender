import eventlet
eventlet.monkey_patch()

import requests
from flask import Flask
from flask_cors import CORS, cross_origin
import json


def setup(app, args):
    app.run(debug=True)

def createFlaskApp():
    # Set up app object
    app = Flask(__name__)


    # Setup some configs for the flask app
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type' 
    app.secret_key = "secretKey!@#$"

    # Setup blueprints
    from Resource.TopicResource import topicBP
    from Resource.ChannelResource import channelBP
    from Resource.TagResource import tagBP


    app.register_blueprint(topicBP, url_prefix="/topic")
    app.register_blueprint(channelBP, url_prefix="/channel")
    app.register_blueprint(tagBP, url_prefix="/tag")

    
    return app
