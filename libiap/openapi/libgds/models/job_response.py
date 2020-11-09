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


class JobResponse(object):
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
        'id': 'str',
        'parent_folder_urn': 'str',
        'operation_type': 'JobOperationType',
        'operation_parameters': 'JobOperationParameters',
        'progress_status': 'JobProgressStatus',
        'time_created': 'datetime',
        'created_by': 'str',
        'time_modified': 'datetime',
        'time_completed': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'parent_folder_urn': 'parentFolderUrn',
        'operation_type': 'operationType',
        'operation_parameters': 'operationParameters',
        'progress_status': 'progressStatus',
        'time_created': 'timeCreated',
        'created_by': 'createdBy',
        'time_modified': 'timeModified',
        'time_completed': 'timeCompleted'
    }

    def __init__(self, id=None, parent_folder_urn=None, operation_type=None, operation_parameters=None, progress_status=None, time_created=None, created_by=None, time_modified=None, time_completed=None, local_vars_configuration=None):  # noqa: E501
        """JobResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._parent_folder_urn = None
        self._operation_type = None
        self._operation_parameters = None
        self._progress_status = None
        self._time_created = None
        self._created_by = None
        self._time_modified = None
        self._time_completed = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if parent_folder_urn is not None:
            self.parent_folder_urn = parent_folder_urn
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_parameters is not None:
            self.operation_parameters = operation_parameters
        if progress_status is not None:
            self.progress_status = progress_status
        if time_created is not None:
            self.time_created = time_created
        if created_by is not None:
            self.created_by = created_by
        if time_modified is not None:
            self.time_modified = time_modified
        if time_completed is not None:
            self.time_completed = time_completed

    @property
    def id(self):
        """Gets the id of this JobResponse.  # noqa: E501

        A unique identifier for this Job  # noqa: E501

        :return: The id of this JobResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobResponse.

        A unique identifier for this Job  # noqa: E501

        :param id: The id of this JobResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_folder_urn(self):
        """Gets the parent_folder_urn of this JobResponse.  # noqa: E501

        The Universal Resource Name of the parent folder associated with the Job  # noqa: E501

        :return: The parent_folder_urn of this JobResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_urn

    @parent_folder_urn.setter
    def parent_folder_urn(self, parent_folder_urn):
        """Sets the parent_folder_urn of this JobResponse.

        The Universal Resource Name of the parent folder associated with the Job  # noqa: E501

        :param parent_folder_urn: The parent_folder_urn of this JobResponse.  # noqa: E501
        :type: str
        """

        self._parent_folder_urn = parent_folder_urn

    @property
    def operation_type(self):
        """Gets the operation_type of this JobResponse.  # noqa: E501


        :return: The operation_type of this JobResponse.  # noqa: E501
        :rtype: JobOperationType
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this JobResponse.


        :param operation_type: The operation_type of this JobResponse.  # noqa: E501
        :type: JobOperationType
        """

        self._operation_type = operation_type

    @property
    def operation_parameters(self):
        """Gets the operation_parameters of this JobResponse.  # noqa: E501


        :return: The operation_parameters of this JobResponse.  # noqa: E501
        :rtype: JobOperationParameters
        """
        return self._operation_parameters

    @operation_parameters.setter
    def operation_parameters(self, operation_parameters):
        """Sets the operation_parameters of this JobResponse.


        :param operation_parameters: The operation_parameters of this JobResponse.  # noqa: E501
        :type: JobOperationParameters
        """

        self._operation_parameters = operation_parameters

    @property
    def progress_status(self):
        """Gets the progress_status of this JobResponse.  # noqa: E501


        :return: The progress_status of this JobResponse.  # noqa: E501
        :rtype: JobProgressStatus
        """
        return self._progress_status

    @progress_status.setter
    def progress_status(self, progress_status):
        """Sets the progress_status of this JobResponse.


        :param progress_status: The progress_status of this JobResponse.  # noqa: E501
        :type: JobProgressStatus
        """

        self._progress_status = progress_status

    @property
    def time_created(self):
        """Gets the time_created of this JobResponse.  # noqa: E501

        The date & time this Folder was created, in GDS  # noqa: E501

        :return: The time_created of this JobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this JobResponse.

        The date & time this Folder was created, in GDS  # noqa: E501

        :param time_created: The time_created of this JobResponse.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def created_by(self):
        """Gets the created_by of this JobResponse.  # noqa: E501

        The creator of this Job  # noqa: E501

        :return: The created_by of this JobResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JobResponse.

        The creator of this Job  # noqa: E501

        :param created_by: The created_by of this JobResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def time_modified(self):
        """Gets the time_modified of this JobResponse.  # noqa: E501

        The date & time this Job was updated, in GDS  # noqa: E501

        :return: The time_modified of this JobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this JobResponse.

        The date & time this Job was updated, in GDS  # noqa: E501

        :param time_modified: The time_modified of this JobResponse.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def time_completed(self):
        """Gets the time_completed of this JobResponse.  # noqa: E501

        The date & time this Job was completed, in GDS  # noqa: E501

        :return: The time_completed of this JobResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """Sets the time_completed of this JobResponse.

        The date & time this Job was completed, in GDS  # noqa: E501

        :param time_completed: The time_completed of this JobResponse.  # noqa: E501
        :type: datetime
        """

        self._time_completed = time_completed

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
        if not isinstance(other, JobResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobResponse):
            return True

        return self.to_dict() != other.to_dict()