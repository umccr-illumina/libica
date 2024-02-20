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

from libica.openapi.libgds.configuration import Configuration


class ObjectContainerSettings(object):
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
        'object_container': 'str',
        'key_prefix': 'str',
        'server_side_encryption_algorithm': 'str',
        'server_side_encryption_key': 'str'
    }

    attribute_map = {
        'object_container': 'objectContainer',
        'key_prefix': 'keyPrefix',
        'server_side_encryption_algorithm': 'serverSideEncryptionAlgorithm',
        'server_side_encryption_key': 'serverSideEncryptionKey'
    }

    def __init__(self, object_container=None, key_prefix=None, server_side_encryption_algorithm=None, server_side_encryption_key=None, local_vars_configuration=None):  # noqa: E501
        """ObjectContainerSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object_container = None
        self._key_prefix = None
        self._server_side_encryption_algorithm = None
        self._server_side_encryption_key = None
        self.discriminator = None

        self.object_container = object_container
        if key_prefix is not None:
            self.key_prefix = key_prefix
        if server_side_encryption_algorithm is not None:
            self.server_side_encryption_algorithm = server_side_encryption_algorithm
        if server_side_encryption_key is not None:
            self.server_side_encryption_key = server_side_encryption_key

    @property
    def object_container(self):
        """Gets the object_container of this ObjectContainerSettings.  # noqa: E501

        The object container name  # noqa: E501

        :return: The object_container of this ObjectContainerSettings.  # noqa: E501
        :rtype: str
        """
        return self._object_container

    @object_container.setter
    def object_container(self, object_container):
        """Sets the object_container of this ObjectContainerSettings.

        The object container name  # noqa: E501

        :param object_container: The object_container of this ObjectContainerSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and object_container is None:  # noqa: E501
            raise ValueError("Invalid value for `object_container`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                object_container is not None and len(object_container) > 63):
            raise ValueError("Invalid value for `object_container`, length must be less than or equal to `63`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                object_container is not None and len(object_container) < 3):
            raise ValueError("Invalid value for `object_container`, length must be greater than or equal to `3`")  # noqa: E501

        self._object_container = object_container

    @property
    def key_prefix(self):
        """Gets the key_prefix of this ObjectContainerSettings.  # noqa: E501

        Key prefix within the bucket for GDS to operate within. Volumes may only be created within this prefix and the given credentials need only authorize  access here. If not set, default is to allow operation on the full container. No leading slash, and must end with a trailing slash.  # noqa: E501

        :return: The key_prefix of this ObjectContainerSettings.  # noqa: E501
        :rtype: str
        """
        return self._key_prefix

    @key_prefix.setter
    def key_prefix(self, key_prefix):
        """Sets the key_prefix of this ObjectContainerSettings.

        Key prefix within the bucket for GDS to operate within. Volumes may only be created within this prefix and the given credentials need only authorize  access here. If not set, default is to allow operation on the full container. No leading slash, and must end with a trailing slash.  # noqa: E501

        :param key_prefix: The key_prefix of this ObjectContainerSettings.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                key_prefix is not None and not re.search(r'^[^\/].*$', key_prefix)):  # noqa: E501
            raise ValueError(r"Invalid value for `key_prefix`, must be a follow pattern or equal to `/^[^\/].*$/`")  # noqa: E501

        self._key_prefix = key_prefix

    @property
    def server_side_encryption_algorithm(self):
        """Gets the server_side_encryption_algorithm of this ObjectContainerSettings.  # noqa: E501

        Used to specify the type of server-side encryption (SSE) to be used on the object provider.  This value is used to determine the Amazon S3 header \"x-amz-server-side-encryption\" value.  For example, specify \"AES256\" for SSE-S3, or \"AWS:KMS\" for SSE-KMS.  By default if none is specified, \"AES256\" will be used.  # noqa: E501

        :return: The server_side_encryption_algorithm of this ObjectContainerSettings.  # noqa: E501
        :rtype: str
        """
        return self._server_side_encryption_algorithm

    @server_side_encryption_algorithm.setter
    def server_side_encryption_algorithm(self, server_side_encryption_algorithm):
        """Sets the server_side_encryption_algorithm of this ObjectContainerSettings.

        Used to specify the type of server-side encryption (SSE) to be used on the object provider.  This value is used to determine the Amazon S3 header \"x-amz-server-side-encryption\" value.  For example, specify \"AES256\" for SSE-S3, or \"AWS:KMS\" for SSE-KMS.  By default if none is specified, \"AES256\" will be used.  # noqa: E501

        :param server_side_encryption_algorithm: The server_side_encryption_algorithm of this ObjectContainerSettings.  # noqa: E501
        :type: str
        """

        self._server_side_encryption_algorithm = server_side_encryption_algorithm

    @property
    def server_side_encryption_key(self):
        """Gets the server_side_encryption_key of this ObjectContainerSettings.  # noqa: E501

        Used to specify the serve-side encryption key that might be associated with the specified server-side encryption algorithm  This value can be the AWS KMS arn key, to be used for the Amazon S3 header \"x-amz-server-side-encryption-aws-kms-key-id\" value  Value will be ignored if encryption is \"AES256\"  # noqa: E501

        :return: The server_side_encryption_key of this ObjectContainerSettings.  # noqa: E501
        :rtype: str
        """
        return self._server_side_encryption_key

    @server_side_encryption_key.setter
    def server_side_encryption_key(self, server_side_encryption_key):
        """Sets the server_side_encryption_key of this ObjectContainerSettings.

        Used to specify the serve-side encryption key that might be associated with the specified server-side encryption algorithm  This value can be the AWS KMS arn key, to be used for the Amazon S3 header \"x-amz-server-side-encryption-aws-kms-key-id\" value  Value will be ignored if encryption is \"AES256\"  # noqa: E501

        :param server_side_encryption_key: The server_side_encryption_key of this ObjectContainerSettings.  # noqa: E501
        :type: str
        """

        self._server_side_encryption_key = server_side_encryption_key

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
        if not isinstance(other, ObjectContainerSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectContainerSettings):
            return True

        return self.to_dict() != other.to_dict()