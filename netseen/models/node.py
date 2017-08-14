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


from sqlalchemy import Column, Integer, String
from netseen.models.table import Table

class Router(Table):
    '''
    router tables
    '''

    __tablename__ = 'Node'
    host_name = Column(String(32), primary_key=True, nullable=False, unique=True)
    local_router_id = Column(Integer, nullable=False)
    as_num = Column(Integer, nullable=False)
    bgpls_id = Column(Integer, nullable=False)
    igp_id = Column(Integer, nullable=False)
    bgpls_id = Column(Integer, nullable=False)
    bgpls_id = Column(Integer, nullable=False)
