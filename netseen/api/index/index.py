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


from flask_restful import Resource
from netseen.lib.response import JsonRes


class Index(Resource):
    '''
    net seen engine info
    '''

    def __init__(self):
        super(Index, self).__init__()

    def get(self):
        '''
        index
        '''
        msg = {
            'status': True,
            'data': {
                'updated': "2017-02-02T00:00:00Z",
                'version': "v1"
            }
        }
        return JsonRes(success=True, content=msg)
