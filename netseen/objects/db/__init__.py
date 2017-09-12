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

from netseen.objects.base import NetseenObject
from netseen.common import ns_except


class NetseenDbObject(NetseenObject):
    """the base netseen database object
    """
    db_model = None

    @classmethod
    def validate_filters(cls, **kwargs):
        """make sure all filter fields is valid.
        """
        bad_filters = {key for key in kwargs if key not in cls.fields}
        if bad_filters:
            bad_filters = ', '.join(bad_filters)
            msg = "'%s' is not supported for filtering" % bad_filters
            raise ns_except.BadRequest(resource='filter', msg=msg)

    @classmethod
    def count(cls, database, validate_filters=False, **kwargs):
        """
        Count the number of objects matching filtering criteria.

        :param database:
        :param validate_filters: Raises an error in case of passing an unknown
                                 filter
        :param kwargs: multiple keys defined by key=value pairs
        :return: number of matching objects
        """
        if validate_filters:
            cls.validate_filters(**kwargs)
        with database.session.begin(subtransactions=True):
            return database.session.query(cls.db_model).filter_by(**kwargs).count()

    @classmethod
    def create_object(cls, database, values):
        """create one object
        """
        with database.session.begin(subtransactions=True):
            db_obj = cls.db_model(**values)
            database.session.add(db_obj)
        return db_obj

    @classmethod
    def get_object(cls, database, **kwargs):
        """get one object, if there is no matched object, it will return None
        """
        with database.session.begin(subtransactions=True):
            return database.session.query(cls.db_model).filter_by(**kwargs).first()

    @classmethod
    def get_objects(cls, database, **kwargs):
        """get objects
        """
        # TODO(penxiao) page function
        with database.session.begin(subtransactions=True):
            return database.session.query(cls.db_model).filter_by(**kwargs).all()

    @classmethod
    def _safe_get_object(cls, database, **kwargs):
        """get one object, if there is no matched, raise exception
        """
        db_obj = cls.get_object(database, **kwargs)

        if db_obj is None:
            key = ", ".join(['%s=%s' % (key, value) for (key, value)
                            in kwargs.items()])
            raise ns_except.ObjectNotFound(id="%s(%s)" % (cls.db_model.__name__, key))
        return db_obj

    @classmethod
    def delete_object(cls, database, **kwargs):
        '''delete one object
        '''
        with database.session.begin(subtransactions=True):
            db_obj = cls._safe_get_object(database, **kwargs)
            database.session.delete(db_obj)
