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

from contextlib import contextmanager
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from netseen.models.interface import Interface  # noqa
from netseen.models.router import Router  # noqa
from netseen.models.node import Node  # noqa
from netseen.models.link import Link  # noqa
from netseen.models.prefix import Prefix  # noqa
from netseen.models.table import BASE
from netseen.common.yaml_parser import YamlParser


class DataBase(object):
    '''
    get DB session
    '''

    def __init__(self, db_url=None, **kwargs):
        if not db_url:
            db_url = os.environ.get(
                'DATABASE_URL', YamlParser().yaml_to_dict().get('DATABASE_URL'))
        self.engine = create_engine(db_url, **kwargs)
        self.session = sessionmaker(self.engine)()

    def create_all(self):
        '''
        create all tables
        '''
        BASE.metadata.create_all(self.engine)

    def drop_all(self):
        '''
        drop all tables
        '''
        BASE.metadata.drop_all(self.engine)

    @contextmanager
    def session_scope(self):
        '''
        session scope
        '''
        session = self.session
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


if __name__ == '__main__':
    pass
