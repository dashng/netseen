#!/usr/bin/env python

from __future__ import print_function
import os
import sys

from flask_script import Manager

from netseen import create_app
# from netseen.extensions import db
from netseen.models.database import DataBase
# from netseen.models.user import User

sys.path.insert(0, os.getcwd())

manager = Manager(create_app)


@manager.command
def createdb(drop_first=False):
    """Creates the database."""
    # if drop_first:
    #     db.drop_all()
    # db.create_all()
    try:
        if drop_first:
            DataBase().drop_all()
        DataBase().create_all()
    except Exception as e:
        print(e)


# @manager.command
# def create_admin():
#     """Creates the admin user."""
#     username = 'admin'
#     password = 'admin'
#     db.session.add(User(username=username, password=password, admin=True))
#     db.session.commit()


if __name__ == '__main__':
    manager.run()
