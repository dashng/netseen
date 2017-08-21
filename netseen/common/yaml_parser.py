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

import json
import os

import yaml

YAML_FILE = os.path.normpath(
    os.path.join(
        os.path.abspath(__file__),
        "../../", "./netseen.yaml"
    )
)


class YamlParser(object):
    '''
    yaml parser util
    '''

    def __init__(self, path=YAML_FILE):
        self._path = path
        self._docs = self._load_yaml()

    def _load_yaml(self):
        stream = open(self._path, "r")
        docs = yaml.load_all(stream)
        return docs

    def yaml_to_dict(self):
        '''
        yaml to dict
        '''
        configs = {}
        for doc in self._docs:
            for k, value in doc.items():
                configs[k] = value
        return configs

    def yaml_to_object(self):
        '''
        yaml data to object
        '''
        def obj():
            return None
        obj.__dict__ = json.loads(json.dumps(self.yaml_to_dict()))
        return obj


if __name__ == "__main__":
    pass
