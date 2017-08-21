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

import ipaddr


class IPFormatter(object):
    '''
    ip formatter
    '''

    def __init__(self):
        pass

    def is_ip(self, *args):
        '''
        validate if is ip
        '''
        try:
            ip_addr = ipaddr.IPAddress(args[0])
            return ip_addr, ip_addr.version
        except ValueError:
            return False
        except StandardError:
            return False

    def ip_int(self, *args):
        '''
        ip str addr to integer
        '''
        try:
            ip_addr = ipaddr.IPAddress(args[0])
            return int(ip_addr)
        except ValueError:
            raise ValueError('Invalid ip string')
        except Exception:
            raise ValueError('Invalid ip string')

    def ip_str(self, *args):
        '''
        ip int to str
        '''
        try:
            ip_addr = ipaddr.IPAddress(args[0])
            return str(ip_addr)
        except ValueError:
            raise ValueError('Invalid ip int')
        except Exception:
            raise ValueError('Invalid ip int')


if __name__ == '__main__':
    IF = IPFormatter()
    print IF.ip_str(3684565272)
