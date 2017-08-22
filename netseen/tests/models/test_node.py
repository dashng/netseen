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


from netseen.tests.db_base import BaseDB
from netseen.models.node import Node


class TestNode(BaseDB):

    def test_add(self):
        node = Node(
            host_name='test',
            local_router_id=12334,
            as_num=100,
            bgpls_id=11111,
            igp_id=222222
        )
        self.session.add(node)
        self.session.commit()
        self.assertEqual(self.session.query(Node).count(), 1)
        self.assertEqual(self.session.query(Node).all(), [node])
