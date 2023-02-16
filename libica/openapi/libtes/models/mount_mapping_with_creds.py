# coding: utf-8

"""
    Task Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from libica.openapi.libtes.configuration import Configuration


class MountMappingWithCreds(object):
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
        'path': 'str',
        'url': 'str',
        'urn': 'str',
        'type': 'str',
        'storage_provider': 'str',
        'credentials': 'dict(str, str)',
        'service_url': 'str'
    }

    attribute_map = {
        'path': 'path',
        'url': 'url',
        'urn': 'urn',
        'type': 'type',
        'storage_provider': 'storageProvider',
        'credentials': 'credentials',
        'service_url': 'serviceUrl'
    }

    def __init__(self, path=None, url=None, urn=None, type=None, storage_provider=None, credentials=None, service_url=None, local_vars_configuration=None):  # noqa: E501
        """MountMappingWithCreds - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._url = None
        self._urn = None
        self._type = None
        self._storage_provider = None
        self._credentials = None
        self._service_url = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if url is not None:
            self.url = url
        if urn is not None:
            self.urn = urn
        if type is not None:
            self.type = type
        if storage_provider is not None:
            self.storage_provider = storage_provider
        if credentials is not None:
            self.credentials = credentials
        if service_url is not None:
            self.service_url = service_url

    @property
    def path(self):
        """Gets the path of this MountMappingWithCreds.  # noqa: E501


        :return: The path of this MountMappingWithCreds.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MountMappingWithCreds.


        :param path: The path of this MountMappingWithCreds.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def url(self):
        """Gets the url of this MountMappingWithCreds.  # noqa: E501


        :return: The url of this MountMappingWithCreds.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MountMappingWithCreds.


        :param url: The url of this MountMappingWithCreds.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def urn(self):
        """Gets the urn of this MountMappingWithCreds.  # noqa: E501


        :return: The urn of this MountMappingWithCreds.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this MountMappingWithCreds.


        :param urn: The urn of this MountMappingWithCreds.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def type(self):
        """Gets the type of this MountMappingWithCreds.  # noqa: E501


        :return: The type of this MountMappingWithCreds.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MountMappingWithCreds.


        :param type: The type of this MountMappingWithCreds.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def storage_provider(self):
        """Gets the storage_provider of this MountMappingWithCreds.  # noqa: E501


        :return: The storage_provider of this MountMappingWithCreds.  # noqa: E501
        :rtype: str
        """
        return self._storage_provider

    @storage_provider.setter
    def storage_provider(self, storage_provider):
        """Sets the storage_provider of this MountMappingWithCreds.


        :param storage_provider: The storage_provider of this MountMappingWithCreds.  # noqa: E501
        :type: str
        """

        self._storage_provider = storage_provider

    @property
    def credentials(self):
        """Gets the credentials of this MountMappingWithCreds.  # noqa: E501


        :return: The credentials of this MountMappingWithCreds.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this MountMappingWithCreds.


        :param credentials: The credentials of this MountMappingWithCreds.  # noqa: E501
        :type: dict(str, str)
        """

        self._credentials = credentials

    @property
    def service_url(self):
        """Gets the service_url of this MountMappingWithCreds.  # noqa: E501


        :return: The service_url of this MountMappingWithCreds.  # noqa: E501
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """Sets the service_url of this MountMappingWithCreds.


        :param service_url: The service_url of this MountMappingWithCreds.  # noqa: E501
        :type: str
        """

        self._service_url = service_url

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
        if not isinstance(other, MountMappingWithCreds):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MountMappingWithCreds):
            return True

        return self.to_dict() != other.to_dict()
