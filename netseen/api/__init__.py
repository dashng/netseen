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

import pkgutil

BLUEP_PRINTS_TYPE = ['BLUE_PRINT', 'BLUE_PRINT_PUBLIC']
BLUEPRINTS = []
__all__ = []

# dynamical load sub blueprints
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    for bpt in BLUEP_PRINTS_TYPE:
        try:
            bp = getattr(module, bpt)
            if bp:
                BLUEPRINTS.append((bp, bpt))
        except AttributeError:
            pass
