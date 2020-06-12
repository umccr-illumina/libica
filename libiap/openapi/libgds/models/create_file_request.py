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


class CreateFileRequest(object):
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
        'volume_id': 'str',
        'folder_path': 'str',
        'type': 'str',
        'volume_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'volume_id': 'volumeId',
        'folder_path': 'folderPath',
        'type': 'type',
        'volume_name': 'volumeName'
    }

    def __init__(self, name=None, volume_id=None, folder_path=None, type=None, volume_name=None, local_vars_configuration=None):  # noqa: E501
        """CreateFileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._volume_id = None
        self._folder_path = None
        self._type = None
        self._volume_name = None
        self.discriminator = None

        self.name = name
        if volume_id is not None:
            self.volume_id = volume_id
        if folder_path is not None:
            self.folder_path = folder_path
        if type is not None:
            self.type = type
        if volume_name is not None:
            self.volume_name = volume_name

    @property
    def name(self):
        """Gets the name of this CreateFileRequest.  # noqa: E501

        Name of the file to be uploaded, case sensitive.  # noqa: E501

        :return: The name of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateFileRequest.

        Name of the file to be uploaded, case sensitive.  # noqa: E501

        :param name: The name of this CreateFileRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[^\/]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^\/]+$/`")  # noqa: E501

        self._name = name

    @property
    def volume_id(self):
        """Gets the volume_id of this CreateFileRequest.  # noqa: E501

        Volume ID to which the file will be uploaded  # noqa: E501

        :return: The volume_id of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this CreateFileRequest.

        Volume ID to which the file will be uploaded  # noqa: E501

        :param volume_id: The volume_id of this CreateFileRequest.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def folder_path(self):
        """Gets the folder_path of this CreateFileRequest.  # noqa: E501

        Optional folder path where the file will be uploaded to  # noqa: E501

        :return: The folder_path of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this CreateFileRequest.

        Optional folder path where the file will be uploaded to  # noqa: E501

        :param folder_path: The folder_path of this CreateFileRequest.  # noqa: E501
        :type: str
        """

        self._folder_path = folder_path

    @property
    def type(self):
        """Gets the type of this CreateFileRequest.  # noqa: E501

        Optional file content type, e.g. text/plain, application/json  # noqa: E501

        :return: The type of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateFileRequest.

        Optional file content type, e.g. text/plain, application/json  # noqa: E501

        :param type: The type of this CreateFileRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def volume_name(self):
        """Gets the volume_name of this CreateFileRequest.  # noqa: E501

        Name of the Volume  # noqa: E501

        :return: The volume_name of this CreateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this CreateFileRequest.

        Name of the Volume  # noqa: E501

        :param volume_name: The volume_name of this CreateFileRequest.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

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
        if not isinstance(other, CreateFileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateFileRequest):
            return True

        return self.to_dict() != other.to_dict()
