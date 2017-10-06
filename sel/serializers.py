#-*- coding:utf-8 -*-
import datetime
import json
import uuid

class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        elif isinstance(o, uuid.UUID):
            return o.hex
        return json.JSONEncoder.default(self, o)
