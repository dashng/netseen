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


class Router(object):
    '''
    router class
    '''

    session = (DataBase().get_session())()

    def __init__(self):
        super(Router, self).__init__()

    def add(self, **kwargs):
        '''
        add router
        '''
        router = RouterTable(**kwargs)
        self.session.add(router)
        self.session.commit()
        self.session.close()

    def delete(self, **kwargs):
        '''
        del router
        '''
        self.session.remove(kwargs)

    def get(self, *args, **kwargs):
        '''
        get router
        '''
        pass


if __name__ == '__main__':
    ROUTER_CLS = Router()
    ARGS = {
        'ip_int': 999900,
        'host_name': 'test_router4',
        'cpu': 80,
        'memory': 999,
        'vendor': 'cisco'
    }
    ROUTER_CLS.add(**ARGS)
