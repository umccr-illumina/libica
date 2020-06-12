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


class FolderUnarchiveRequest(object):
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
        'restore_speed': 'str'
    }

    attribute_map = {
        'restore_speed': 'restoreSpeed'
    }

    def __init__(self, restore_speed=None, local_vars_configuration=None):  # noqa: E501
        """FolderUnarchiveRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._restore_speed = None
        self.discriminator = None

        self.restore_speed = restore_speed

    @property
    def restore_speed(self):
        """Gets the restore_speed of this FolderUnarchiveRequest.  # noqa: E501

        The desired Restore Speed to move the Files in the Folder to the Standard Storage Tier. Valid values are Economy and Standard.  # noqa: E501

        :return: The restore_speed of this FolderUnarchiveRequest.  # noqa: E501
        :rtype: str
        """
        return self._restore_speed

    @restore_speed.setter
    def restore_speed(self, restore_speed):
        """Sets the restore_speed of this FolderUnarchiveRequest.

        The desired Restore Speed to move the Files in the Folder to the Standard Storage Tier. Valid values are Economy and Standard.  # noqa: E501

        :param restore_speed: The restore_speed of this FolderUnarchiveRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and restore_speed is None:  # noqa: E501
            raise ValueError("Invalid value for `restore_speed`, must not be `None`")  # noqa: E501

        self._restore_speed = restore_speed

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
        if not isinstance(other, FolderUnarchiveRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderUnarchiveRequest):
            return True

        return self.to_dict() != other.to_dict()
