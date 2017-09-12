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

from netseen.tests import db_base
from netseen.objects.db.node import Node


class TestNode(db_base.BaseDB):
    """Test class for node object
    """
    def test_field_none_nullable(self):
        """test field could not be null
        """
        node_dict = {
            'host_name': 'abc'
        }
        try:
            Node(**node_dict)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_field_nullable(self):
        """test field could be none
        """
        node_dict = {
            'host_name': 'abc',
            'local_router_id': '1.1.1.1',
            'as_num': 100,
            'bgpls_id': '0.0.0.0',
            'igp_id': '0.0.0.0'
        }
        node = Node(**node_dict)
        for name, field in node_dict.items():
            self.assertEqual(field, node.__dict__[name])

    def test_invalid_field_type(self):
        """invalid field value type: ip address format error
        """
        node_dict = {
            'host_name': 'abc',
            'local_router_id': '1.1.1.500',
            'as_num': 100,
            'bgpls_id': '0.0.0.0',
            'igp_id': '0.0.0.0'
        }
        try:
            Node(**node_dict)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_create_get_delete_node(self):
        """create, get, delete node from database
        """
        node_dict_1 = {
            'host_name': 'abc',
            'local_router_id': '1.1.1.1',
            'as_num': 100,
            'bgpls_id': '0.0.0.0',
            'igp_id': '0.0.0.0'
        }
        node_dict_2 = {
            'host_name': 'def',
            'local_router_id': '2.2.2.2',
            'as_num': 100,
            'bgpls_id': '0.0.0.0',
            'igp_id': '0.0.0.0'
        }

        # create two objects
        node1 = Node(**node_dict_1)
        node2 = Node(**node_dict_2)
        Node.create_object(self.database, node1.__dict__)
        Node.create_object(self.database, node2.__dict__)
        self.assertEqual(2, Node.count(self.database))

        # get one object
        node1 = Node.get_object(self.database, host_name='abc')
        self.assertEqual(node_dict_1['local_router_id'], node1.__dict__['local_router_id'])

        # get objects
        nodes = Node.get_objects(self.database, as_num=100)
        self.assertEqual(2, len(nodes))

        # delete objects
        Node.delete_object(self.database, host_name='abc')
        self.assertEqual(1, Node.count(self.database))
