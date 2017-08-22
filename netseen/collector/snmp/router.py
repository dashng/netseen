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
    from netseen.common.ip_conversion import IPConversion
    from netseen.common.snmp_poller import SnmpPoller
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
    from netseen.common.ip_conversion import IPConversion
    from netseen.common.snmp_poller import SnmpPoller


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
        :ip_int: ip int format
        :host_name: router host_name
        :cpu: cpu
        :memory: memory
        :vendor: router vendor
        '''
        router = RouterTable(**kwargs)
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
        :filters: {attrs...}
        :values: {values...}
        '''
        filters = kwargs.get('filters')
        values = kwargs.get('values')
        with (self.database.session_scope()) as session:
            session.query(RouterTable).filter_by(**filters).update(values)

    def get_db_model(self):
        '''
        get database object, router table model
        '''
        return self.database, RouterTable

    def poll_ifaces(self, router_ip, community):
        '''
        poll router ifaces
        '''
        poller = SnmpPoller(router_ip=router_ip, community=community)
        oid = poller.get_oid('if_list')
        ifaces = poller.get_mib_by_oid(oid)
        ifaces = [
            {
                'oid': (iface[0]).split('.')[-1],
                'name': iface[1]
            }
            for iface in ifaces]
        return ifaces

    def poll_iface_ip(self, router_ip, community):
        '''
        poll iface ip
        '''
        poller = SnmpPoller(router_ip=router_ip, community=community)
        oid = poller.get_oid('if_ip')
        ifaces_ip = poller.get_mib_by_oid(oid)
        ifaces_ip = [
            {
                'ip': '.'.join((iface[0]).split('.')[-4:]),
                'oid': iface[1]
            }
            for iface in ifaces_ip]
        return ifaces_ip

    def poll_iface_speed(self, router_ip, community, if_oid):
        '''
        poll iface speed
        '''
        poller = SnmpPoller(router_ip=router_ip, community=community)
        oid = poller.get_oid('if_speed')
        ifaces_speed = poller.get_mib_by_oid(oid % if_oid)
        ifaces = [
            {
                'oid': (iface[0]).split('.')[-1],
                'speed': iface[1]
            }
            for iface in ifaces_speed]
        return ifaces

    def poll_router_hostname(self, router_ip, community):
        '''
        poll router host name
        '''
        poller = SnmpPoller(router_ip=router_ip, community=community)
        oid = poller.get_oid('sys_name')
        router = poller.get_mib_by_oid(oid)
        if not router:
            return None
        return router.pop()[1]

    def poll_router_vendor(self, router_ip, community):
        '''
        poll router vendor
        '''
        poller = SnmpPoller(router_ip=router_ip, community=community)
        oid = poller.get_oid('vendor')
        router = poller.get_mib_by_oid(oid)
        if not router:
            return None
        return router.pop()[1]

    def poll_router_memory(self, router_ip, community):
        '''
        poll router memory
        '''
        poller = SnmpPoller(router_ip=router_ip, community=community)
        # # oid = poller.get_oid('vendor')
        # oid = '1.3.6.1.4.1.2021.4.3.0'
        # router = poller.get_mib_by_oid(oid)
        # if not router:
        #     return None
        # return router.pop()[1]
        return 11

    def poll_router_cpu(self, router_ip, community):
        '''
        poll router memory
        '''
        poller = SnmpPoller(router_ip=router_ip, community=community)
        # # oid = poller.get_oid('vendor')
        # oid = '1.3.6.1.4.1.2021.4.3.0'
        # router = poller.get_mib_by_oid(oid)
        # if not router:
        #     return None
        # return router.pop()[1] 
        return 500



if __name__ == '__main__':
    ROUTER_CLS = Router()
    # ARGS = {
    #     'ip_int': 999900,
    #     'host_name': 'test_router4',
    #     'cpu': 80,
    #     'memory': 999,
    #     'vendor': 'cisco'
    # }
    # ROUTER_CLS.add(**ARGS)
    # print ROUTER_CLS.get(ip_int=999900)
    # ROUTER_CLS.delete(ip_int=999900)
    # print ROUTER_CLS.poll_ifaces('10.75.44.119', 'cisco')
    # print ROUTER_CLS.poll_iface_speed('10.75.44.119', 'cisco', '3')
    # print ROUTER_CLS.poll_iface_ip('10.75.44.119', 'cisco')
    # print ROUTER_CLS.poll_router_hostname('10.75.44.119', 'cisco')
    # print ROUTER_CLS.poll_router_vendor('10.75.44.119', 'cisco')
    print ROUTER_CLS.poll_router_memory('10.75.44.119', 'cisco')
