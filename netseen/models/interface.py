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


class Interface(Table):
    '''
    router tables
    '''
    __tablename__ = 'Interface'
    ip_int = Column(
        Integer, primary_key=True, nullable=False, unique=True)
    iface_oid = Column(
        Integer, primary_key=True, nullable=False, unique=False)
    iface_name = Column(
        String(32), nullable=False)
    speed = Column(Integer, nullable=False)
    router_ip_int = Column(
        Integer, ForeignKey("Router.ip_int"), nullable=False)

    # def __init__(self, ip_int=None, \
    #     iface_oid=None, iface_name=None, \
    #     speed=None, router_ip_int=None, created_on=None, updated_on=None):
    #     '''
    #     model init
    #     '''
    #     self.ip_int = ip_int
    #     self.iface_oid = iface_oid
    #     self.iface_name = iface_name
    #     self.speed = speed
    #     self.router_ip_int = router_ip_int
    #     self.created_on = created_on
    #     self.updated_on = updated_on
