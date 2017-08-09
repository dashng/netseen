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

from base import BaseTestCase


class TestUser(BaseTestCase):

    def test_user(self):

        # create a new user
        r, s, h = self.post('/api/users', data={'username': 'foo',
                                                'password': 'bar'})
        self.assertEqual(s, 201)
        url = h['Location']
        self.assertEqual(url, 'http://localhost/api/users/1')

        # get users without auth
        r, s, h = self.get('/api/users')
        self.assertEqual(s, 200)

        # get users with bad auth
        r, s, h = self.get('/api/users', token_auth='bad-token')
        self.assertEqual(s, 401)
