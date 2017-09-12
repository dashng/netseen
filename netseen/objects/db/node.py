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

from netseen.models import node
from netseen.objects.db import NetseenDbObject
from netseen.objects import fields


class Node(NetseenDbObject):
    """Node object
    """
    db_model = node.Node
    fields = {
        'host_name': fields.StringField(),
        'local_router_id': fields.IPAddressField(),
        'as_num': fields.IntegerField(),
        'bgpls_id': fields.StringField(),
        'igp_id': fields.StringField(),
        'ospf_id': fields.StringField(nullable=True)
    }
