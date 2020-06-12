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


class CreateVolumeResponse(object):
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
        'name': 'str',
        'tenant_id': 'str',
        'sub_tenant_id': 'str',
        'urn': 'str',
        'inherited_acl': 'list[str]',
        'time_created': 'datetime',
        'created_by': 'str',
        'time_modified': 'datetime',
        'modified_by': 'str',
        'job_status': 'JobStatus',
        'temporary_upload_credentials': 'ObjectStorageCredentialsResponse',
        'object_store_access': 'ObjectStoreAccess'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tenant_id': 'tenantId',
        'sub_tenant_id': 'subTenantId',
        'urn': 'urn',
        'inherited_acl': 'inheritedAcl',
        'time_created': 'timeCreated',
        'created_by': 'createdBy',
        'time_modified': 'timeModified',
        'modified_by': 'modifiedBy',
        'job_status': 'jobStatus',
        'temporary_upload_credentials': 'temporaryUploadCredentials',
        'object_store_access': 'objectStoreAccess'
    }

    def __init__(self, id=None, name=None, tenant_id=None, sub_tenant_id=None, urn=None, inherited_acl=None, time_created=None, created_by=None, time_modified=None, modified_by=None, job_status=None, temporary_upload_credentials=None, object_store_access=None, local_vars_configuration=None):  # noqa: E501
        """CreateVolumeResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._tenant_id = None
        self._sub_tenant_id = None
        self._urn = None
        self._inherited_acl = None
        self._time_created = None
        self._created_by = None
        self._time_modified = None
        self._modified_by = None
        self._job_status = None
        self._temporary_upload_credentials = None
        self._object_store_access = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if sub_tenant_id is not None:
            self.sub_tenant_id = sub_tenant_id
        if urn is not None:
            self.urn = urn
        if inherited_acl is not None:
            self.inherited_acl = inherited_acl
        if time_created is not None:
            self.time_created = time_created
        if created_by is not None:
            self.created_by = created_by
        if time_modified is not None:
            self.time_modified = time_modified
        if modified_by is not None:
            self.modified_by = modified_by
        if job_status is not None:
            self.job_status = job_status
        if temporary_upload_credentials is not None:
            self.temporary_upload_credentials = temporary_upload_credentials
        if object_store_access is not None:
            self.object_store_access = object_store_access

    @property
    def id(self):
        """Gets the id of this CreateVolumeResponse.  # noqa: E501

        A unique identifier for this Volume  # noqa: E501

        :return: The id of this CreateVolumeResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateVolumeResponse.

        A unique identifier for this Volume  # noqa: E501

        :param id: The id of this CreateVolumeResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateVolumeResponse.  # noqa: E501

        The name of this Volume  # noqa: E501

        :return: The name of this CreateVolumeResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVolumeResponse.

        The name of this Volume  # noqa: E501

        :param name: The name of this CreateVolumeResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateVolumeResponse.  # noqa: E501

        The unique identifier for this Volume's Tenant  # noqa: E501

        :return: The tenant_id of this CreateVolumeResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateVolumeResponse.

        The unique identifier for this Volume's Tenant  # noqa: E501

        :param tenant_id: The tenant_id of this CreateVolumeResponse.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this CreateVolumeResponse.  # noqa: E501

        The unique identifier for this Volume's Sub Tenant  # noqa: E501

        :return: The sub_tenant_id of this CreateVolumeResponse.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this CreateVolumeResponse.

        The unique identifier for this Volume's Sub Tenant  # noqa: E501

        :param sub_tenant_id: The sub_tenant_id of this CreateVolumeResponse.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def urn(self):
        """Gets the urn of this CreateVolumeResponse.  # noqa: E501

        The Universal Resource Name, unique to this Volume  # noqa: E501

        :return: The urn of this CreateVolumeResponse.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this CreateVolumeResponse.

        The Universal Resource Name, unique to this Volume  # noqa: E501

        :param urn: The urn of this CreateVolumeResponse.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def inherited_acl(self):
        """Gets the inherited_acl of this CreateVolumeResponse.  # noqa: E501

        The inherited list of Id(s) that have access to this Volume  # noqa: E501

        :return: The inherited_acl of this CreateVolumeResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._inherited_acl

    @inherited_acl.setter
    def inherited_acl(self, inherited_acl):
        """Sets the inherited_acl of this CreateVolumeResponse.

        The inherited list of Id(s) that have access to this Volume  # noqa: E501

        :param inherited_acl: The inherited_acl of this CreateVolumeResponse.  # noqa: E501
        :type: list[str]
        """

        self._inherited_acl = inherited_acl

    @property
    def time_created(self):
        """Gets the time_created of this CreateVolumeResponse.  # noqa: E501

        The date & time this Volume was created, in GDS  # noqa: E501

        :return: The time_created of this CreateVolumeResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this CreateVolumeResponse.

        The date & time this Volume was created, in GDS  # noqa: E501

        :param time_created: The time_created of this CreateVolumeResponse.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def created_by(self):
        """Gets the created_by of this CreateVolumeResponse.  # noqa: E501

        The creator of this Volume  # noqa: E501

        :return: The created_by of this CreateVolumeResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CreateVolumeResponse.

        The creator of this Volume  # noqa: E501

        :param created_by: The created_by of this CreateVolumeResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def time_modified(self):
        """Gets the time_modified of this CreateVolumeResponse.  # noqa: E501

        The date & time this Volume was updated, in GDS  # noqa: E501

        :return: The time_modified of this CreateVolumeResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this CreateVolumeResponse.

        The date & time this Volume was updated, in GDS  # noqa: E501

        :param time_modified: The time_modified of this CreateVolumeResponse.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def modified_by(self):
        """Gets the modified_by of this CreateVolumeResponse.  # noqa: E501

        The updator of this Volume  # noqa: E501

        :return: The modified_by of this CreateVolumeResponse.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this CreateVolumeResponse.

        The updator of this Volume  # noqa: E501

        :param modified_by: The modified_by of this CreateVolumeResponse.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def job_status(self):
        """Gets the job_status of this CreateVolumeResponse.  # noqa: E501


        :return: The job_status of this CreateVolumeResponse.  # noqa: E501
        :rtype: JobStatus
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this CreateVolumeResponse.


        :param job_status: The job_status of this CreateVolumeResponse.  # noqa: E501
        :type: JobStatus
        """

        self._job_status = job_status

    @property
    def temporary_upload_credentials(self):
        """Gets the temporary_upload_credentials of this CreateVolumeResponse.  # noqa: E501


        :return: The temporary_upload_credentials of this CreateVolumeResponse.  # noqa: E501
        :rtype: ObjectStorageCredentialsResponse
        """
        return self._temporary_upload_credentials

    @temporary_upload_credentials.setter
    def temporary_upload_credentials(self, temporary_upload_credentials):
        """Sets the temporary_upload_credentials of this CreateVolumeResponse.


        :param temporary_upload_credentials: The temporary_upload_credentials of this CreateVolumeResponse.  # noqa: E501
        :type: ObjectStorageCredentialsResponse
        """

        self._temporary_upload_credentials = temporary_upload_credentials

    @property
    def object_store_access(self):
        """Gets the object_store_access of this CreateVolumeResponse.  # noqa: E501


        :return: The object_store_access of this CreateVolumeResponse.  # noqa: E501
        :rtype: ObjectStoreAccess
        """
        return self._object_store_access

    @object_store_access.setter
    def object_store_access(self, object_store_access):
        """Sets the object_store_access of this CreateVolumeResponse.


        :param object_store_access: The object_store_access of this CreateVolumeResponse.  # noqa: E501
        :type: ObjectStoreAccess
        """

        self._object_store_access = object_store_access

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
        if not isinstance(other, CreateVolumeResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateVolumeResponse):
            return True

        return self.to_dict() != other.to_dict()
