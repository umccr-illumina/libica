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


class JobOutput(object):
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
        'folder_copy': 'FileCopyOutput',
        'file_copy': 'FileCopyOutput',
        'folder_metadata_update_output': 'MetadataUpdateOutput',
        'file_metadata_update_output': 'MetadataUpdateOutput',
        'file_move': 'FileMoveOutput',
        'folder_move': 'FileMoveOutput'
    }

    attribute_map = {
        'folder_copy': 'folderCopy',
        'file_copy': 'fileCopy',
        'folder_metadata_update_output': 'folderMetadataUpdateOutput',
        'file_metadata_update_output': 'fileMetadataUpdateOutput',
        'file_move': 'fileMove',
        'folder_move': 'folderMove'
    }

    def __init__(self, folder_copy=None, file_copy=None, folder_metadata_update_output=None, file_metadata_update_output=None, file_move=None, folder_move=None, local_vars_configuration=None):  # noqa: E501
        """JobOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._folder_copy = None
        self._file_copy = None
        self._folder_metadata_update_output = None
        self._file_metadata_update_output = None
        self._file_move = None
        self._folder_move = None
        self.discriminator = None

        if folder_copy is not None:
            self.folder_copy = folder_copy
        if file_copy is not None:
            self.file_copy = file_copy
        if folder_metadata_update_output is not None:
            self.folder_metadata_update_output = folder_metadata_update_output
        if file_metadata_update_output is not None:
            self.file_metadata_update_output = file_metadata_update_output
        if file_move is not None:
            self.file_move = file_move
        if folder_move is not None:
            self.folder_move = folder_move

    @property
    def folder_copy(self):
        """Gets the folder_copy of this JobOutput.  # noqa: E501


        :return: The folder_copy of this JobOutput.  # noqa: E501
        :rtype: FileCopyOutput
        """
        return self._folder_copy

    @folder_copy.setter
    def folder_copy(self, folder_copy):
        """Sets the folder_copy of this JobOutput.


        :param folder_copy: The folder_copy of this JobOutput.  # noqa: E501
        :type: FileCopyOutput
        """

        self._folder_copy = folder_copy

    @property
    def file_copy(self):
        """Gets the file_copy of this JobOutput.  # noqa: E501


        :return: The file_copy of this JobOutput.  # noqa: E501
        :rtype: FileCopyOutput
        """
        return self._file_copy

    @file_copy.setter
    def file_copy(self, file_copy):
        """Sets the file_copy of this JobOutput.


        :param file_copy: The file_copy of this JobOutput.  # noqa: E501
        :type: FileCopyOutput
        """

        self._file_copy = file_copy

    @property
    def folder_metadata_update_output(self):
        """Gets the folder_metadata_update_output of this JobOutput.  # noqa: E501


        :return: The folder_metadata_update_output of this JobOutput.  # noqa: E501
        :rtype: MetadataUpdateOutput
        """
        return self._folder_metadata_update_output

    @folder_metadata_update_output.setter
    def folder_metadata_update_output(self, folder_metadata_update_output):
        """Sets the folder_metadata_update_output of this JobOutput.


        :param folder_metadata_update_output: The folder_metadata_update_output of this JobOutput.  # noqa: E501
        :type: MetadataUpdateOutput
        """

        self._folder_metadata_update_output = folder_metadata_update_output

    @property
    def file_metadata_update_output(self):
        """Gets the file_metadata_update_output of this JobOutput.  # noqa: E501


        :return: The file_metadata_update_output of this JobOutput.  # noqa: E501
        :rtype: MetadataUpdateOutput
        """
        return self._file_metadata_update_output

    @file_metadata_update_output.setter
    def file_metadata_update_output(self, file_metadata_update_output):
        """Sets the file_metadata_update_output of this JobOutput.


        :param file_metadata_update_output: The file_metadata_update_output of this JobOutput.  # noqa: E501
        :type: MetadataUpdateOutput
        """

        self._file_metadata_update_output = file_metadata_update_output

    @property
    def file_move(self):
        """Gets the file_move of this JobOutput.  # noqa: E501


        :return: The file_move of this JobOutput.  # noqa: E501
        :rtype: FileMoveOutput
        """
        return self._file_move

    @file_move.setter
    def file_move(self, file_move):
        """Sets the file_move of this JobOutput.


        :param file_move: The file_move of this JobOutput.  # noqa: E501
        :type: FileMoveOutput
        """

        self._file_move = file_move

    @property
    def folder_move(self):
        """Gets the folder_move of this JobOutput.  # noqa: E501


        :return: The folder_move of this JobOutput.  # noqa: E501
        :rtype: FileMoveOutput
        """
        return self._folder_move

    @folder_move.setter
    def folder_move(self, folder_move):
        """Sets the folder_move of this JobOutput.


        :param folder_move: The folder_move of this JobOutput.  # noqa: E501
        :type: FileMoveOutput
        """

        self._folder_move = folder_move

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
        if not isinstance(other, JobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobOutput):
            return True

        return self.to_dict() != other.to_dict()
