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


class FileMoveOutput(object):
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
        'items_skipped_count': 'int',
        'items_failed_count': 'int',
        'items_moved_count': 'int',
        'folders_moved_count': 'int',
        'elastic_indexing_matched': 'bool',
        'items_failed': 'list[BulkFailedItem]'
    }

    attribute_map = {
        'items_skipped_count': 'itemsSkippedCount',
        'items_failed_count': 'itemsFailedCount',
        'items_moved_count': 'itemsMovedCount',
        'folders_moved_count': 'foldersMovedCount',
        'elastic_indexing_matched': 'elasticIndexingMatched',
        'items_failed': 'itemsFailed'
    }

    def __init__(self, items_skipped_count=None, items_failed_count=None, items_moved_count=None, folders_moved_count=None, elastic_indexing_matched=None, items_failed=None, local_vars_configuration=None):  # noqa: E501
        """FileMoveOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._items_skipped_count = None
        self._items_failed_count = None
        self._items_moved_count = None
        self._folders_moved_count = None
        self._elastic_indexing_matched = None
        self._items_failed = None
        self.discriminator = None

        if items_skipped_count is not None:
            self.items_skipped_count = items_skipped_count
        if items_failed_count is not None:
            self.items_failed_count = items_failed_count
        if items_moved_count is not None:
            self.items_moved_count = items_moved_count
        if folders_moved_count is not None:
            self.folders_moved_count = folders_moved_count
        if elastic_indexing_matched is not None:
            self.elastic_indexing_matched = elastic_indexing_matched
        if items_failed is not None:
            self.items_failed = items_failed

    @property
    def items_skipped_count(self):
        """Gets the items_skipped_count of this FileMoveOutput.  # noqa: E501


        :return: The items_skipped_count of this FileMoveOutput.  # noqa: E501
        :rtype: int
        """
        return self._items_skipped_count

    @items_skipped_count.setter
    def items_skipped_count(self, items_skipped_count):
        """Sets the items_skipped_count of this FileMoveOutput.


        :param items_skipped_count: The items_skipped_count of this FileMoveOutput.  # noqa: E501
        :type: int
        """

        self._items_skipped_count = items_skipped_count

    @property
    def items_failed_count(self):
        """Gets the items_failed_count of this FileMoveOutput.  # noqa: E501


        :return: The items_failed_count of this FileMoveOutput.  # noqa: E501
        :rtype: int
        """
        return self._items_failed_count

    @items_failed_count.setter
    def items_failed_count(self, items_failed_count):
        """Sets the items_failed_count of this FileMoveOutput.


        :param items_failed_count: The items_failed_count of this FileMoveOutput.  # noqa: E501
        :type: int
        """

        self._items_failed_count = items_failed_count

    @property
    def items_moved_count(self):
        """Gets the items_moved_count of this FileMoveOutput.  # noqa: E501


        :return: The items_moved_count of this FileMoveOutput.  # noqa: E501
        :rtype: int
        """
        return self._items_moved_count

    @items_moved_count.setter
    def items_moved_count(self, items_moved_count):
        """Sets the items_moved_count of this FileMoveOutput.


        :param items_moved_count: The items_moved_count of this FileMoveOutput.  # noqa: E501
        :type: int
        """

        self._items_moved_count = items_moved_count

    @property
    def folders_moved_count(self):
        """Gets the folders_moved_count of this FileMoveOutput.  # noqa: E501


        :return: The folders_moved_count of this FileMoveOutput.  # noqa: E501
        :rtype: int
        """
        return self._folders_moved_count

    @folders_moved_count.setter
    def folders_moved_count(self, folders_moved_count):
        """Sets the folders_moved_count of this FileMoveOutput.


        :param folders_moved_count: The folders_moved_count of this FileMoveOutput.  # noqa: E501
        :type: int
        """

        self._folders_moved_count = folders_moved_count

    @property
    def elastic_indexing_matched(self):
        """Gets the elastic_indexing_matched of this FileMoveOutput.  # noqa: E501


        :return: The elastic_indexing_matched of this FileMoveOutput.  # noqa: E501
        :rtype: bool
        """
        return self._elastic_indexing_matched

    @elastic_indexing_matched.setter
    def elastic_indexing_matched(self, elastic_indexing_matched):
        """Sets the elastic_indexing_matched of this FileMoveOutput.


        :param elastic_indexing_matched: The elastic_indexing_matched of this FileMoveOutput.  # noqa: E501
        :type: bool
        """

        self._elastic_indexing_matched = elastic_indexing_matched

    @property
    def items_failed(self):
        """Gets the items_failed of this FileMoveOutput.  # noqa: E501


        :return: The items_failed of this FileMoveOutput.  # noqa: E501
        :rtype: list[BulkFailedItem]
        """
        return self._items_failed

    @items_failed.setter
    def items_failed(self, items_failed):
        """Sets the items_failed of this FileMoveOutput.


        :param items_failed: The items_failed of this FileMoveOutput.  # noqa: E501
        :type: list[BulkFailedItem]
        """

        self._items_failed = items_failed

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
        if not isinstance(other, FileMoveOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileMoveOutput):
            return True

        return self.to_dict() != other.to_dict()
