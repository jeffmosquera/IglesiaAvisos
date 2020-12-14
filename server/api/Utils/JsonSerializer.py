import json
from datetime import date, datetime

from bson.objectid import ObjectId


class JsonSerializer:

    @staticmethod
    def converter(obj):
        if isinstance(obj, (datetime, date)):
            return str(obj)
        if isinstance(obj, ObjectId):
            return str(obj)

    @classmethod
    def serialize(cls, obj):
        json_dumps = json.dumps(obj, default=cls.converter)
        return json.loads(json_dumps)
