import json
import uuid
from bson import ObjectId, Timestamp, json_util
from datetime import datetime

class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId) or isinstance(o, Timestamp) or isinstance(o, bytes) or isinstance(o, uuid.UUID) \
            or isinstance(o, datetime):
                return str(o)
        return json.JSONEncoder.default(self, o)

