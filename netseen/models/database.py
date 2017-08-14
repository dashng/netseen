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

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from netseen.models.router import Router
from netseen.models.table import BASE


class DataBase(object):
    '''
    get DB session
    '''
    def __init__(self):
        super(DataBase, self).__init__()

    def get_engine(self):
        '''
        create db engine
        '''
        engine = create_engine('mysql+pymysql://root:cisco123@localhost:3306/test')
        return engine

    def get_session(self):
        '''
        get db session
        '''
        engine = self.get_engine()
        return sessionmaker(bind=engine)

    def create_all(self):
        '''
        create all tables
        '''
        BASE.metadata.create_all(self.get_engine())

if __name__ == '__main__':
    pass
