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

try:
    from netseen.models.router import Router as RouterTable
    from netseen.models.database import DataBase
except ImportError:
    import os
    import sys
    PATH = os.path.normpath(
        os.path.join(
            os.path.abspath(__file__),
            "../../../../", ""
        )
    )
    sys.path.insert(0, PATH)
    from netseen.models.router import Router as RouterTable
    from netseen.models.database import DataBase

def test():
    yield '0000'


class Router(object):
    '''
    router class
    '''

    database = DataBase()

    def __init__(self):
        super(Router, self).__init__()

    def add(self, **kwargs):
        '''
        add router
        '''
        router = RouterTable(**kwargs)
        with (self.database.session_scope()) as session:
            session.add(router)

    def delete(self, **kwargs):
        '''
        del router
        '''
        with (self.database.session_scope()) as session:
            session.query(RouterTable).filter_by(**kwargs).delete()

    def get(self, **kwargs):
        '''
        get router
        '''
        routers = None
        with (self.database.session_scope()) as session:
            routers = session.query(RouterTable).filter_by(**kwargs).all()
        return routers

    def update(self, **kwargs):
        '''
        update router
        '''
        filters = kwargs.get('filters')
        values = kwargs.get('values')
        with (self.database.session_scope()) as session:
            session.query(RouterTable).filter_by(**filters).update(values)


if __name__ == '__main__':
    ROUTER_CLS = Router()
    ARGS = {
        'ip_int': 999900,
        'host_name': 'test_router4',
        'cpu': 80,
        'memory': 999,
        'vendor': 'cisco'
    }
    # ROUTER_CLS.add(**ARGS)
    print ROUTER_CLS.get(ip_int=999900)
    # ROUTER_CLS.delete(ip_int=999900)
