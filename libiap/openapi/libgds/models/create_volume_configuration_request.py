# coding: utf-8

"""
    Genomic Data Store Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from libiap.openapi.libgds.configuration import Configuration


class CreateVolumeConfigurationRequest(object):
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
        'name': 'str',
        'object_store_settings': 'ObjectStoreSettings'
    }

    attribute_map = {
        'name': 'name',
        'object_store_settings': 'objectStoreSettings'
    }

    def __init__(self, name=None, object_store_settings=None, local_vars_configuration=None):  # noqa: E501
        """CreateVolumeConfigurationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._object_store_settings = None
        self.discriminator = None

        self.name = name
        self.object_store_settings = object_store_settings

    @property
    def name(self):
        """Gets the name of this CreateVolumeConfigurationRequest.  # noqa: E501

        Name for the volume configuration  # noqa: E501

        :return: The name of this CreateVolumeConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVolumeConfigurationRequest.

        Name for the volume configuration  # noqa: E501

        :param name: The name of this CreateVolumeConfigurationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def object_store_settings(self):
        """Gets the object_store_settings of this CreateVolumeConfigurationRequest.  # noqa: E501


        :return: The object_store_settings of this CreateVolumeConfigurationRequest.  # noqa: E501
        :rtype: ObjectStoreSettings
        """
        return self._object_store_settings

    @object_store_settings.setter
    def object_store_settings(self, object_store_settings):
        """Sets the object_store_settings of this CreateVolumeConfigurationRequest.


        :param object_store_settings: The object_store_settings of this CreateVolumeConfigurationRequest.  # noqa: E501
        :type: ObjectStoreSettings
        """
        if self.local_vars_configuration.client_side_validation and object_store_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `object_store_settings`, must not be `None`")  # noqa: E501

        self._object_store_settings = object_store_settings

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
        if not isinstance(other, CreateVolumeConfigurationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVolumeConfigurationRequest):
            return True

        return self.to_dict() != other.to_dict()
