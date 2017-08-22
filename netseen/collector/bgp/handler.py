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

from __future__ import print_function
import logging
import os

from oslo_config import cfg
from yabgp.handler import BaseHandler

from netseen.models.database import DataBase

CONF = cfg.CONF

LOG = logging.getLogger(__name__)

MSG_PROCESS_OPTS = [
    cfg.StrOpt(
        'connection',
        default=os.environ.get(
            'DATABASE_URL', 'mysql+pymysql://root:root@localhost:3306/test'),
        # secret=True,
        help='database connection url'
    )
]

CONF.register_cli_opts(MSG_PROCESS_OPTS, group='database')


class TopoHandler(BaseHandler):
    """Topology Handler
    """

    def __init__(self):
        super(TopoHandler, self).__init__()
        self.db_session = None

    def init(self):
        """some init stuff"""
        LOG.info('init database session')
        self.db_session = DataBase(db_url=CONF.database.connection).get_session()

    def on_update_error(self, peer, timestamp, msg):
        print('[-] UPDATE ERROR,', msg)

    def route_refresh_received(self, peer, msg, msg_type):
        print('[+] ROUTE_REFRESH received,', msg)

    def keepalive_received(self, peer, timestamp):
        print('[+] KEEPALIVE received')

    def open_received(self, peer, timestamp, result):
        print('[+] OPEN received,', result)

    def update_received(self, peer, timestamp, msg):
        print('[+] UPDATE received,', msg)

    def notification_received(self, peer, msg):
        print('[-] NOTIFICATION received,', msg)

    def on_connection_lost(self, peer):
        print('[-] CONNECTION lost')

    def on_connection_failed(self, peer, msg):
        print('[-] CONNECTION failed,', msg)
