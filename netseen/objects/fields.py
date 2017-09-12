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

import abc

import six
import netaddr


class AbstractFieldType(object):
    """abstract field type class
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def constraint(self, obj, attr, value):
        '''this method is called to convert the given value into the designated type,
        or throw an exception if this is not possible.

        :param:obj: The NetseenDbObject on which an attribute is being set
        :param:attr: The name of the attribute being set
        :param:value: The value being set
        :returns: A properly-typed value
        '''
        pass


class Field(object):
    """base field class
    """

    def __init__(self, field_type, nullable=False):
        self._type = field_type
        self._nullable = nullable

    @property
    def nullable(self):
        """property for if this field is nullable
        """
        return self._nullable

    def _null(self, obj, attr):
        """process field value is None
        """
        if self.nullable:
            return None
        else:
            raise ValueError("Field '%s' of object '%s' cannot be None" % (attr, obj))

    def constraint(self, obj, attr, value):
        """make sure field value is valid
        """
        if value is None:
            return self._null(obj, attr)
        else:
            return self._type.constraint(obj, attr, value)


class String(AbstractFieldType):
    """string format filed type
    """
    @staticmethod
    def constraint(obj, attr, value):
        """make sure the field value is string or converted to string
        """
        accepted_types = six.string_types + six.integer_types

        if isinstance(value, accepted_types):
            return six.text_type(value)
        else:
            raise ValueError(
                'A string is required in field %(attr)s, not a %(type)s' %
                {'attr': attr, 'type': type(value).__name__}
            )


class Integer(AbstractFieldType):
    """interger format field type
    """
    @staticmethod
    def constraint(obj, attr, value):
        return int(value)


class Boolean(AbstractFieldType):
    """bool format field type
    """
    @staticmethod
    def constraint(obj, attr, value):
        return bool(value)


class IPAddress(AbstractFieldType):
    """ip address field type
    """
    @staticmethod
    def constraint(obj, attr, value):
        try:
            return netaddr.IPAddress(value).__str__()
        except netaddr.AddrFormatError as e:
            raise ValueError(six.text_type(e))


class IPV4Address(IPAddress):
    """ipv4 address field type
    """
    @staticmethod
    def constraint(obj, attr, value):
        result = IPAddress.constraint(obj, attr, value)
        if result.version != 4:
            raise ValueError('Network "%(val)s" is not valid '
                             'in field %(attr)s' %
                             {'val': value, 'attr': attr})
        return result


class AutoTypedField(Field):
    AUTO_TYPE = None

    def __init__(self, **kwargs):
        super(AutoTypedField, self).__init__(self.AUTO_TYPE, **kwargs)


class StringField(AutoTypedField):
    AUTO_TYPE = String()


class IntegerField(AutoTypedField):
    AUTO_TYPE = Integer()


class BooleanField(AutoTypedField):
    AUTO_TYPE = Boolean()


class IPAddressField(AutoTypedField):
    AUTO_TYPE = IPAddress()
