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

from sqlalchemy import Column, Integer, String, ForeignKey

from netseen.models.table import Table


class Prefix(Table):
    '''
    router tables
    '''

    __tablename__ = 'Prefix'
    prefix = Column(String(32), primary_key=True, nullable=False, unique=True)
    prefix_sid = Column(Integer, nullable=True)
    prefix_metric = Column(Integer, nullable=False)
    # host_name = Column(String(32), nullable=False, unique=True)
    host_name = Column(String(32), ForeignKey(
        'Node.host_name'), nullable=False)
