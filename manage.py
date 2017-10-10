#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import unittest

from flask_script import Manager

from netseen import create_app
from netseen.database import DataBase

sys.path.insert(0, os.getcwd())

manager = Manager(create_app)


@manager.command
def createdb(drop_first=False):
    """Creates the database."""
    try:
        if drop_first:
            DataBase().drop_all()
        DataBase().create_all()
    except Exception as e:
        print(e)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('netseen.tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

# @manager.command
# def create_admin():
#     """Creates the admin user."""
#     username = 'admin'
#     password = 'admin'
#     db.session.add(User(username=username, password=password, admin=True))
#     db.session.commit()


if __name__ == '__main__':
    manager.run()
