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

import sqlalchemy

from netseen.tests import db_base
from netseen.objects.db.prefix import Prefix
from netseen.objects.db.node import Node


class TestPrefox(db_base.BaseDB):
    """Test class for prefix object
    """

    def setUp(self):

        self.prefix_dict1 = {
            'prefix': '1.1.1.1/32',
            'prefix_metric': 100,
            'prefix_sid': 2000,
            'host_name': 'abc'
        }
        self.node_dict = {
            'host_name': 'abc',
            'local_router_id': '1.1.1.1',
            'as_num': 100,
            'bgpls_id': '0.0.0.0',
            'igp_id': '0.0.0.0'
        }
        db_base.BaseDB.setUp(self)

    def test_field_none_nullable(self):
        """test field could not be none
        """
        self.prefix_dict1.pop('prefix_metric')
        try:
            Prefix(**self.prefix_dict1)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_field_nullable(self):
        """test field could be none
        """

        self.prefix_dict1.pop('prefix_sid')
        prefix_obj = Prefix(**self.prefix_dict1)
        for key in self.prefix_dict1:
            self.assertEqual(
                self.prefix_dict1[key], prefix_obj.__dict__.get(key))

    def test_invalid_host_name(self):
        """test invalid hostname, invalid ForeignKey
        """
        prefix_obj = Prefix(**self.prefix_dict1)
        try:
            Prefix.create_object(self.database, prefix_obj.__dict__)
        except Exception as e:
            self.assertEqual(sqlalchemy.exc.IntegrityError, type(e))

    def test_valid_host_name(self):
        """test valid host name, valid ForeignKey
        """
        node_db_obj = Node.create_object(self.database, Node(**self.node_dict).__dict__)

        self.prefix_dict1['host_name'] = node_db_obj.get('host_name')
        prefix_db_obj = Prefix.create_object(
            self.database, Prefix(**self.prefix_dict1).__dict__)
        self.assertEqual(1, Prefix.count(self.database, host_name=node_db_obj.get('host_name')))
        self.assertEqual(prefix_db_obj.get('host_name'), node_db_obj.get('host_name'))
