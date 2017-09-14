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

from netseen.models import link
from netseen.objects.db import NetseenDbObject
from netseen.objects import fields


class Link(NetseenDbObject):
    """Link object
    """
    db_model = link.Link
    fields = {
        'link_local_ipv4': fields.IPAddressField(),
        'link_remote_ipv4': fields.IPAddressField(),
        'adj_segment_id': fields.IntegerField(nullable=True),
        'metric_igp': fields.IntegerField(nullable=True),
        'metric_te': fields.IntegerField(nullable=True),
        'max_bandwidth': fields.IntegerField(nullable=True),
        'max_rsv_bandwidth': fields.IntegerField(nullable=True)
    }
