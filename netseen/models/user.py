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

"""User Model
"""

import os
import binascii

from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash

from netseen.extensions import db
from netseen.utils import timestamp, url_for


class User(db.Model):

    """The User model."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=timestamp)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    token = db.Column(db.String(64), nullable=True, unique=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def password(self):
        """password can not be read"""
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        self.token = None  # if user is changing passwords, also revoke token

    def verify_password(self, password):
        """Check password"""
        return check_password_hash(self.password_hash, password)

    def generate_token(self):
        """Creates a 64 character long randomly generated token."""
        self.token = binascii.hexlify(os.urandom(32)).decode('utf-8')
        return self.token

    @staticmethod
    def create(data):
        """Create a new user."""
        user = User()
        user.from_dict(data, partial_update=False)
        return user

    def from_dict(self, data, partial_update=True):
        """Import user data from a dictionary."""
        for field in ['username', 'password']:
            try:
                setattr(self, field, data[field])
            except KeyError:
                if not partial_update:
                    abort(400)

    def to_dict(self):
        """Export user to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at,
            'username': self.username,
            'admin': self.admin,
            'token': self.token,
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'tokens': url_for('api.new_token')
            }
        }
