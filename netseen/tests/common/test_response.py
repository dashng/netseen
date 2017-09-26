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

import unittest
import json
import datetime

from netseen.common.response import JsonRes


class TestJsonResponse(unittest.TestCase):
    """Test json response encode
    """

    def test_with_datatime_filed(self):

        t_now = datetime.datetime.now()
        json_res = JsonRes(data={'time': t_now})
        self.assertEqual(200, json_res.status_code)
        self.assertEqual(True, t_now.isoformat() in json_res.data)

    def test_with_exception_filed(self):

        error = ValueError('error message')
        json_res = JsonRes(success=False, info=error)
        dict_res = json.loads(json_res.data)
        self.assertEqual(error.__class__.__name__, dict_res['meta']['info']['exception'])

    def test_simple_type(self):

        JsonRes(success=True, data={1: 1, 2: 2})
