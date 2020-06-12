# coding: utf-8

"""
    Developer Console Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from libiap.openapi.libconsole.configuration import Configuration


class ProductUsage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'amount': 'float',
        'unit': 'str',
        'i_credit': 'float'
    }

    attribute_map = {
        'type': 'type',
        'amount': 'amount',
        'unit': 'unit',
        'i_credit': 'iCredit'
    }

    def __init__(self, type=None, amount=None, unit=None, i_credit=None, local_vars_configuration=None):  # noqa: E501
        """ProductUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._amount = None
        self._unit = None
        self._i_credit = None
        self.discriminator = None

        self.type = type
        self.amount = amount
        self.unit = unit
        if i_credit is not None:
            self.i_credit = i_credit

    @property
    def type(self):
        """Gets the type of this ProductUsage.  # noqa: E501


        :return: The type of this ProductUsage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductUsage.


        :param type: The type of this ProductUsage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this ProductUsage.  # noqa: E501


        :return: The amount of this ProductUsage.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ProductUsage.


        :param amount: The amount of this ProductUsage.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def unit(self):
        """Gets the unit of this ProductUsage.  # noqa: E501


        :return: The unit of this ProductUsage.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ProductUsage.


        :param unit: The unit of this ProductUsage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unit is None:  # noqa: E501
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501

        self._unit = unit

    @property
    def i_credit(self):
        """Gets the i_credit of this ProductUsage.  # noqa: E501


        :return: The i_credit of this ProductUsage.  # noqa: E501
        :rtype: float
        """
        return self._i_credit

    @i_credit.setter
    def i_credit(self, i_credit):
        """Sets the i_credit of this ProductUsage.


        :param i_credit: The i_credit of this ProductUsage.  # noqa: E501
        :type: float
        """

        self._i_credit = i_credit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductUsage):
            return True

        return self.to_dict() != other.to_dict()
