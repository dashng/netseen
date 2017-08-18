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

from pysnmp.hlapi import \
    bulkCmd, getCmd, nextCmd, SnmpEngine, CommunityData, UdpTransportTarget, \
    ContextData, ObjectType, ObjectIdentity, UsmUserData


class SnmpPoll(object):
    '''
    Snmp Mib Poller
    v2c:
    :router_ip: device ip string format
    :community: snmp community
    v3:
    :user_name: user name auth
    :auth_key: auth key auth
    :priv_key: privacy key auth
    :version: snmp verison ['2c', '3']
    :snmp_port: default set to be 161
    '''
    SNMP_VERSION_2C = '2c'
    SNMP_VERSION_3 = '3'
    snmp_ret = None
    router_ip = None
    community = None
    snmp_port = 161
    user_name = None
    auth_key = None
    priv_key = None
    version = None

    def __init__(self, **kwargs):
        super(SnmpPoll, self).__init__()
        cls_ = type(self)
        for k in kwargs:
            if not hasattr(cls_, k):
                raise TypeError(
                    "%r is an invalid keyword argument for %s" %
                    (k, cls_.__name__))
            setattr(self, k, kwargs[k])

    def _to_list(self):
        '''
        parse snmp return & return list
        '''
        mib_ret = []
        for (error_indication,
             error_status,
             error_index,
             var_binds) in self.snmp_ret:
            if error_indication:
                break
            elif error_status:
                print('%s at %s' % (error_status.prettyPrint(),
                                    error_index and var_binds[int(error_index) - 1][0] or '?'))
                break
            else:
                for var_bind in var_binds:
                    mib_ret.append([x.prettyPrint() for x in var_bind])
        return mib_ret

    def get_auth(self):
        '''
        get auth by snmp version
        '''
        auth = None
        if self.version == self.SNMP_VERSION_2C:
            auth = CommunityData(self.community)
        elif self.version == self.SNMP_VERSION_3:
            auth = UsmUserData(self.user_name,
                               authKey=self.auth_key, privKey=self.priv_key)
        return auth

    def next_cmd(self, oid, max_rows=25, max_calls=0):
        '''
        get next oid mib info
        '''
        self.snmp_ret = nextCmd(SnmpEngine(),
                                CommunityData(self.community),
                                UdpTransportTarget(
                                    (self.router_ip, self.snmp_port)),
                                ContextData(),
                                ObjectType(ObjectIdentity(oid)),
                                maxRows=max_rows, maxCalls=max_calls)
        return self._to_list()

    def get_cmd(self, oid):
        '''
        get oid mib info
        '''
        self.snmp_ret = getCmd(SnmpEngine(),
                               self.get_auth(),
                               UdpTransportTarget(
                                   (self.router_ip, self.snmp_port)),
                               ContextData(),
                               ObjectType(ObjectIdentity(oid)))
        return self._to_list()

    def bulk_cmd(self, oid, non_repeaters=0, max_repeaters=1):
        '''
        bulk get router info by oid
        '''
        self.snmp_ret = bulkCmd(SnmpEngine(),
                                CommunityData(self.community),
                                UdpTransportTarget(
                                    (self.router_ip, self.snmp_port)),
                                ContextData(),
                                non_repeaters, max_repeaters,
                                ObjectType(ObjectIdentity(oid)),
                                maxCalls=10)
        return self._to_list()


if __name__ == '__main__':
    snmp_poll = SnmpPoll(router_ip='10.75.44.119', community='cisco')
    print snmp_poll.next_cmd('1.3.6.1.2.1.2.2.1.2')
    # print snmp_poll.bulk_cmd('1.3.6.1.2.1.2.2.1.2')
    # print snmp_poll.get_cmd('1.3.6.1.2.1.2.2.1.2')
