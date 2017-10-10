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

from sqlalchemy import orm

from netseen.models.node import Node


class TestNodeModel(unittest.TestCase):
    """Test class for node model
    """

    def setUp(self):
        self.node_dict = {
            'host_name': 'abc',
            'local_router_id': '1.1.1.1',
            'as_num': 100,
            'bgpls_id': '0.0.0.0',
            'igp_id': '0.0.0.0',
        }

    def test_update(self):
        node = Node(**self.node_dict)
        new_as_num = 200
        node.update({'as_num': new_as_num})
        self.assertEqual(new_as_num, node.get('as_num'))

    def test_items_keys(self):
        node = Node(**self.node_dict)
        key_list = [column.name for column in orm.object_mapper(node).columns]
        key_list.sort()
        node_keys = node.keys()
        node_keys.sort()
        self.assertEqual(key_list, node_keys)

        for key, _ in node:
            self.assertEqual(True, key in key_list)

        for key, _ in node.items():
            self.assertEqual(True, key in key_list)
