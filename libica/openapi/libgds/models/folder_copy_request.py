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


class FolderCopyRequest(object):
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
        'target_parent_folder_id': 'str',
        'destination_folder_name': 'str',
        'metadata_to_copy': 'list[str]',
        'metadata_to_update': 'object',
        'metadata_items_to_add': 'object',
        'metadata_items_to_delete': 'object',
        'duplicate_file_action': 'str'
    }

    attribute_map = {
        'target_parent_folder_id': 'targetParentFolderId',
        'destination_folder_name': 'destinationFolderName',
        'metadata_to_copy': 'metadataToCopy',
        'metadata_to_update': 'metadataToUpdate',
        'metadata_items_to_add': 'metadataItemsToAdd',
        'metadata_items_to_delete': 'metadataItemsToDelete',
        'duplicate_file_action': 'duplicateFileAction'
    }

    def __init__(self, target_parent_folder_id=None, destination_folder_name=None, metadata_to_copy=None, metadata_to_update=None, metadata_items_to_add=None, metadata_items_to_delete=None, duplicate_file_action=None, local_vars_configuration=None):  # noqa: E501
        """FolderCopyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_parent_folder_id = None
        self._destination_folder_name = None
        self._metadata_to_copy = None
        self._metadata_to_update = None
        self._metadata_items_to_add = None
        self._metadata_items_to_delete = None
        self._duplicate_file_action = None
        self.discriminator = None

        self.target_parent_folder_id = target_parent_folder_id
        if destination_folder_name is not None:
            self.destination_folder_name = destination_folder_name
        if metadata_to_copy is not None:
            self.metadata_to_copy = metadata_to_copy
        if metadata_to_update is not None:
            self.metadata_to_update = metadata_to_update
        if metadata_items_to_add is not None:
            self.metadata_items_to_add = metadata_items_to_add
        if metadata_items_to_delete is not None:
            self.metadata_items_to_delete = metadata_items_to_delete
        if duplicate_file_action is not None:
            self.duplicate_file_action = duplicate_file_action

    @property
    def target_parent_folder_id(self):
        """Gets the target_parent_folder_id of this FolderCopyRequest.  # noqa: E501

        The parent folder into which the source folder will be copied.  # noqa: E501

        :return: The target_parent_folder_id of this FolderCopyRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_parent_folder_id

    @target_parent_folder_id.setter
    def target_parent_folder_id(self, target_parent_folder_id):
        """Sets the target_parent_folder_id of this FolderCopyRequest.

        The parent folder into which the source folder will be copied.  # noqa: E501

        :param target_parent_folder_id: The target_parent_folder_id of this FolderCopyRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_parent_folder_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_parent_folder_id`, must not be `None`")  # noqa: E501

        self._target_parent_folder_id = target_parent_folder_id

    @property
    def destination_folder_name(self):
        """Gets the destination_folder_name of this FolderCopyRequest.  # noqa: E501

        A new name for the destination folder. Required if target parent folder is the same as the destination folder.  When optional and not provided, the source folder name is used as the destination folder name.  # noqa: E501

        :return: The destination_folder_name of this FolderCopyRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_folder_name

    @destination_folder_name.setter
    def destination_folder_name(self, destination_folder_name):
        """Sets the destination_folder_name of this FolderCopyRequest.

        A new name for the destination folder. Required if target parent folder is the same as the destination folder.  When optional and not provided, the source folder name is used as the destination folder name.  # noqa: E501

        :param destination_folder_name: The destination_folder_name of this FolderCopyRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                destination_folder_name is not None and not re.search(r'^[^\/]+$', destination_folder_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `destination_folder_name`, must be a follow pattern or equal to `/^[^\/]+$/`")  # noqa: E501

        self._destination_folder_name = destination_folder_name

    @property
    def metadata_to_copy(self):
        """Gets the metadata_to_copy of this FolderCopyRequest.  # noqa: E501

        List of metadata to be copied/kept  # noqa: E501

        :return: The metadata_to_copy of this FolderCopyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._metadata_to_copy

    @metadata_to_copy.setter
    def metadata_to_copy(self, metadata_to_copy):
        """Sets the metadata_to_copy of this FolderCopyRequest.

        List of metadata to be copied/kept  # noqa: E501

        :param metadata_to_copy: The metadata_to_copy of this FolderCopyRequest.  # noqa: E501
        :type: list[str]
        """

        self._metadata_to_copy = metadata_to_copy

    @property
    def metadata_to_update(self):
        """Gets the metadata_to_update of this FolderCopyRequest.  # noqa: E501

        Modifies the contents of existing metadata  # noqa: E501

        :return: The metadata_to_update of this FolderCopyRequest.  # noqa: E501
        :rtype: object
        """
        return self._metadata_to_update

    @metadata_to_update.setter
    def metadata_to_update(self, metadata_to_update):
        """Sets the metadata_to_update of this FolderCopyRequest.

        Modifies the contents of existing metadata  # noqa: E501

        :param metadata_to_update: The metadata_to_update of this FolderCopyRequest.  # noqa: E501
        :type: object
        """

        self._metadata_to_update = metadata_to_update

    @property
    def metadata_items_to_add(self):
        """Gets the metadata_items_to_add of this FolderCopyRequest.  # noqa: E501

        Add an item to a metadata with array type  # noqa: E501

        :return: The metadata_items_to_add of this FolderCopyRequest.  # noqa: E501
        :rtype: object
        """
        return self._metadata_items_to_add

    @metadata_items_to_add.setter
    def metadata_items_to_add(self, metadata_items_to_add):
        """Sets the metadata_items_to_add of this FolderCopyRequest.

        Add an item to a metadata with array type  # noqa: E501

        :param metadata_items_to_add: The metadata_items_to_add of this FolderCopyRequest.  # noqa: E501
        :type: object
        """

        self._metadata_items_to_add = metadata_items_to_add

    @property
    def metadata_items_to_delete(self):
        """Gets the metadata_items_to_delete of this FolderCopyRequest.  # noqa: E501

        Delete an item from a metadata with array type  # noqa: E501

        :return: The metadata_items_to_delete of this FolderCopyRequest.  # noqa: E501
        :rtype: object
        """
        return self._metadata_items_to_delete

    @metadata_items_to_delete.setter
    def metadata_items_to_delete(self, metadata_items_to_delete):
        """Sets the metadata_items_to_delete of this FolderCopyRequest.

        Delete an item from a metadata with array type  # noqa: E501

        :param metadata_items_to_delete: The metadata_items_to_delete of this FolderCopyRequest.  # noqa: E501
        :type: object
        """

        self._metadata_items_to_delete = metadata_items_to_delete

    @property
    def duplicate_file_action(self):
        """Gets the duplicate_file_action of this FolderCopyRequest.  # noqa: E501


        :return: The duplicate_file_action of this FolderCopyRequest.  # noqa: E501
        :rtype: str
        """
        return self._duplicate_file_action

    @duplicate_file_action.setter
    def duplicate_file_action(self, duplicate_file_action):
        """Sets the duplicate_file_action of this FolderCopyRequest.


        :param duplicate_file_action: The duplicate_file_action of this FolderCopyRequest.  # noqa: E501
        :type: str
        """

        self._duplicate_file_action = duplicate_file_action

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
        if not isinstance(other, FolderCopyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderCopyRequest):
            return True

        return self.to_dict() != other.to_dict()
