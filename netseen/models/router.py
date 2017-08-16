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
from sqlalchemy.orm import relationship

from netseen.models.table import Table


class Router(Table):
    '''
    router tables
    '''
    __tablename__ = 'Router'
    ip_int = Column(Integer, primary_key=True, nullable=False, unique=True)
    host_name = Column(String(32), nullable=False, unique=True)
    cpu = Column(Integer, nullable=False)
    memory = Column(Integer, nullable=False)
    vendor = Column(String(32), nullable=False)
    interfaces = relationship("Interface")
    nodes = relationship('Node')
    prefix = relationship('Prefix')
