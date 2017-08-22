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

from netseen.common.ip_conversion import IPConversion
from netseen.common.snmp_poller import SnmpPoller
from netseen.models.database import DataBase
from netseen.models.interface import Interface as InterfaceTable


class Interface(object):
    '''
    interface class
    '''

    database = DataBase()

    def __init__(self):
        super(Interface, self).__init__()

    def add(self, **kwargs):
        '''
        add router
        '''
        router = InterfaceTable(**kwargs)
        ip_int = kwargs.get('ip_int')
        ip_str = IPConversion().int_to_str(ip_int)
        SnmpPoller(router_ip=ip_str, community="")
        with (self.database.session_scope()) as session:
            session.add(router)

    def delete(self, **kwargs):
        '''
        del router
        '''
        with (self.database.session_scope()) as session:
            session.query(InterfaceTable).filter_by(**kwargs).delete()

    def get(self, **kwargs):
        '''
        get router
        '''
        routers = None
        with (self.database.session_scope()) as session:
            routers = session.query(InterfaceTable).filter_by(**kwargs).all()
        return routers

    def update(self, **kwargs):
        '''
        update router
        :filters: {attrs...}
        :values: {values...}
        '''
        filters = kwargs.get('filters')
        values = kwargs.get('values')
        with (self.database.session_scope()) as session:
            session.query(InterfaceTable).filter_by(**filters).update(values)

    def get_db_model(self):
        '''
        get database object, router table model
        '''
        return self.database, InterfaceTable

if __name__ == '__main__':
    pass
