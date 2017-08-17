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


from flask import Blueprint
from flask_restful import Api


def blue_print(blue_print_name, template_folder, resources):
    '''
    blue print
    '''
    bpt = Blueprint(blue_print_name, __name__, template_folder=template_folder)

    api = Api(bpt)

    for res in resources:
        if isinstance(res, list):
            api.add_resource(*res)
        else:
            api.add_resource(*res['args'], **res['kwargs'])

    return bpt
