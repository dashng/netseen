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

from netseen.config import config
from netseen.extensions import db

# Import models so that they are registered with SQLAlchemy
# from . import models  # noqa


def create_app(config_name=None):
    """create application"""
    if config_name is None:
        config_name = os.environ.get('NETSEEN_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize flask extensions
    db.init_app(app)

    # Register blueprint
    from netseen.index import main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from netseen.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
