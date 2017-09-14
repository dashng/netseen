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
from netseen.objects.db.link import Link


class TestLink(db_base.BaseDB):
    """Test class for link object
    """

    def test_field_none_nullable(self):
        """test field could not be none
        """
        link_dict = {
            'link_local_ipv4': '1.1.1.1'
        }
        try:
            Link(**link_dict)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_field_nullable(self):
        """test field could be none
        """
        link_dict = {
            'link_local_ipv4': '1.1.1.1',
            'link_remote_ipv4': '2.2.2.2'
        }
        link = Link(**link_dict)
        self.assertEqual(link_dict['link_local_ipv4'], link.__dict__['link_local_ipv4'])
        self.assertEqual(link_dict.get('adj_segment_id'), link.__dict__['adj_segment_id'])
