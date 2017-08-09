#!/usr/bin/env python

import os
import sys
import unittest

sys.path.insert(0, os.getcwd())

from flask_script import Manager

from netseen import create_app
from netseen.extensions import db
from netseen.models.user import User

manager = Manager(create_app)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


@manager.command
def createdb(drop_first=False):
    """Creates the database."""
    if drop_first:
        db.drop_all()
    db.create_all()


@manager.command
def create_admin():
    """Creates the admin user."""
    username = 'admin'
    password = 'admin'
    db.session.add(User(username=username, password=password, admin=True))
    db.session.commit()


if __name__ == '__main__':
    manager.run()
