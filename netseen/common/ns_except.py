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


class NetseenException(Exception):
    '''
    customize exception
    '''
    message = 'An unknown exception occurred'

    def __init__(self, **kwargs):
        try:
            super(NetseenException, self).__init__(self.message % kwargs)
            self.msg = self.message % kwargs
        except Exception:
            # at least get the core message out if something happened
            super(NetseenException, self).__init__(self.message)

    def __unicode__(self):
        return unicode(self.msg)

    def log(self):
        '''
        log except msg
        '''
        pass


class NotFound(NetseenException):
    """A generic not found exception."""
    pass


class BadRequest(NetseenException):
    """An exception indicating a generic bad request for a said resource.

    A generic exception indicating a bad request for a specified resource.
    """
    message = 'Bad %(resource)s request: %(msg)s.'


class ObjectFieldInvalid(NetseenException):
    """the field value of object is invalid
    """
    message = "Field %(field)s of %(objname)s is not an instance of Field"


class Conflict(NetseenException):
    """A generic conflict exception."""
    pass


class NotAuthorized(NetseenException):
    """A generic not authorized exception."""
    message = "Not authorized."


class ServiceUnavailable(NetseenException):
    """A generic service unavailable exception."""
    message = "The service is unavailable."


class ObjectNotFound(NotFound):
    """A not found exception indicating an identifiable object isn't found.

    A specialization of the NotFound exception indicating an object with a said
    ID doesn't exist.

    :param id: The ID of the (not found) object.
    """
    message = "Object %(id)s not found."
