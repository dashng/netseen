# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
as-cnp-dev@cisco.com
Copyright 2015-2016 Cisco Systems, Inc.
All rights reserved.
'''

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
            