import json
import uuid
from bson import ObjectId, Timestamp, json_util

class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId) or isinstance(o, Timestamp) or isinstance(o, bytes) or isinstance(o, uuid.UUID) \
            or isinstance(o, datetime):

            return json.JSONEncoder.default(self, o)

