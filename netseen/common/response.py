# Copyright 2015-2017 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import datetime
import json

import six
from flask import Response

_SIMPLE_TYPE = ((six.text_type,) + six.integer_types + (type(None), bool, float))


def json_encoder(value):
    """Handy for JSON serialization
    """
    if isinstance(value, _SIMPLE_TYPE):
        return value
    if isinstance(value, datetime.datetime):
        return value.isoformat() + "Z"
    elif isinstance(value, Exception):
        return {
            "exception": value.__class__.__name__,
            "message": value.message,
        }
    return str(value)


class JsonRes(Response):
    '''
    json response
    '''

    def __init__(self, data=None, success=True, info=None, code=None):
        self.res = {
            "meta": {
                "status": success,
                "info": info, "code": code},
            "data": data}
        content = json.dumps(self.res, default=json_encoder)
        super(JsonRes, self).__init__(content, status=200,
                                      mimetype="application/json")
