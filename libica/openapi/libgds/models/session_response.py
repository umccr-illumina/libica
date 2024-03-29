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


class SessionResponse(object):
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
        'folder_urn': 'str',
        'status': 'SessionStatus',
        'time_created': 'datetime',
        'time_credentials_expire': 'datetime',
        'time_closed': 'datetime',
        'time_completed': 'datetime',
        'metadata': 'object'
    }

    attribute_map = {
        'id': 'id',
        'folder_urn': 'folderUrn',
        'status': 'status',
        'time_created': 'timeCreated',
        'time_credentials_expire': 'timeCredentialsExpire',
        'time_closed': 'timeClosed',
        'time_completed': 'timeCompleted',
        'metadata': 'metadata'
    }

    def __init__(self, id=None, folder_urn=None, status=None, time_created=None, time_credentials_expire=None, time_closed=None, time_completed=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """SessionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._folder_urn = None
        self._status = None
        self._time_created = None
        self._time_credentials_expire = None
        self._time_closed = None
        self._time_completed = None
        self._metadata = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if folder_urn is not None:
            self.folder_urn = folder_urn
        if status is not None:
            self.status = status
        if time_created is not None:
            self.time_created = time_created
        if time_credentials_expire is not None:
            self.time_credentials_expire = time_credentials_expire
        if time_closed is not None:
            self.time_closed = time_closed
        if time_completed is not None:
            self.time_completed = time_completed
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this SessionResponse.  # noqa: E501

        A unique identifier for this Session  # noqa: E501

        :return: The id of this SessionResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SessionResponse.

        A unique identifier for this Session  # noqa: E501

        :param id: The id of this SessionResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def folder_urn(self):
        """Gets the folder_urn of this SessionResponse.  # noqa: E501

        The Universal Resource Name of the Folder associated with the Session  # noqa: E501

        :return: The folder_urn of this SessionResponse.  # noqa: E501
        :rtype: str
        """
        return self._folder_urn

    @folder_urn.setter
    def folder_urn(self, folder_urn):
        """Sets the folder_urn of this SessionResponse.

        The Universal Resource Name of the Folder associated with the Session  # noqa: E501

        :param folder_urn: The folder_urn of this SessionResponse.  # noqa: E501
        :type: str
        """

        self._folder_urn = folder_urn

    @property
    def status(self):
        """Gets the status of this SessionResponse.  # noqa: E501


        :return: The status of this SessionResponse.  # noqa: E501
        :rtype: SessionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SessionResponse.


        :param status: The status of this SessionResponse.  # noqa: E501
        :type: SessionStatus
        """

        self._status = status

    @property
    def time_created(self):
        """Gets the time_created of this SessionResponse.  # noqa: E501

        The date & time this Session was created, in GDS  # noqa: E501

        :return: The time_created of this SessionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this SessionResponse.

        The date & time this Session was created, in GDS  # noqa: E501

        :param time_created: The time_created of this SessionResponse.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_credentials_expire(self):
        """Gets the time_credentials_expire of this SessionResponse.  # noqa: E501

        The date & time this upload session expires  # noqa: E501

        :return: The time_credentials_expire of this SessionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_credentials_expire

    @time_credentials_expire.setter
    def time_credentials_expire(self, time_credentials_expire):
        """Sets the time_credentials_expire of this SessionResponse.

        The date & time this upload session expires  # noqa: E501

        :param time_credentials_expire: The time_credentials_expire of this SessionResponse.  # noqa: E501
        :type: datetime
        """

        self._time_credentials_expire = time_credentials_expire

    @property
    def time_closed(self):
        """Gets the time_closed of this SessionResponse.  # noqa: E501

        The date & time this Session was closed, in GDS  # noqa: E501

        :return: The time_closed of this SessionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_closed

    @time_closed.setter
    def time_closed(self, time_closed):
        """Sets the time_closed of this SessionResponse.

        The date & time this Session was closed, in GDS  # noqa: E501

        :param time_closed: The time_closed of this SessionResponse.  # noqa: E501
        :type: datetime
        """

        self._time_closed = time_closed

    @property
    def time_completed(self):
        """Gets the time_completed of this SessionResponse.  # noqa: E501

        The date & time this Session was completed, in GDS  # noqa: E501

        :return: The time_completed of this SessionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """Sets the time_completed of this SessionResponse.

        The date & time this Session was completed, in GDS  # noqa: E501

        :param time_completed: The time_completed of this SessionResponse.  # noqa: E501
        :type: datetime
        """

        self._time_completed = time_completed

    @property
    def metadata(self):
        """Gets the metadata of this SessionResponse.  # noqa: E501


        :return: The metadata of this SessionResponse.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SessionResponse.


        :param metadata: The metadata of this SessionResponse.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

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
        if not isinstance(other, SessionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionResponse):
            return True

        return self.to_dict() != other.to_dict()
