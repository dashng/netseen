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

import os
from flask import Flask
from netseen.common.yaml_parser import YamlParser
# from netseen.config import config
from netseen.api import BLUEPRINTS


def create_app(config_name=None):
    '''
    create flask application
    '''
    # if config_name is None:
    #     config_name = os.environ.get('NETSEEN_CONFIG', 'development')
    app = Flask(__name__)

    cfg_file_path = \
        os.path.normpath(
            os.path.join(
                os.path.abspath(__file__),
                "../", "./app.yaml"))

    cfg_object = YamlParser(path=cfg_file_path).yaml_to_object()
    app.config.from_object(cfg_object)
    for blueprint in BLUEPRINTS:
        url_prefix = '/' if blueprint[1] == 'BLUE_PRINT_PUBLIC' else '/api'
        app.register_blueprint(blueprint[0], url_prefix=url_prefix)
    return app
