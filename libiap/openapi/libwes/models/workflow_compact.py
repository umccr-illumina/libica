# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from libiap.openapi.libwes.configuration import Configuration


class WorkflowCompact(object):
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
        'href': 'str',
        'name': 'str',
        'organization': 'str',
        'description': 'str',
        'category': 'str',
        'tool_class': 'str',
        'time_created': 'datetime',
        'time_modified': 'datetime',
        'created_by': 'str',
        'modified_by': 'str',
        'tenant_id': 'str',
        'acl': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'name': 'name',
        'organization': 'organization',
        'description': 'description',
        'category': 'category',
        'tool_class': 'toolClass',
        'time_created': 'timeCreated',
        'time_modified': 'timeModified',
        'created_by': 'createdBy',
        'modified_by': 'modifiedBy',
        'tenant_id': 'tenantId',
        'acl': 'acl'
    }

    def __init__(self, id=None, href=None, name=None, organization=None, description=None, category=None, tool_class=None, time_created=None, time_modified=None, created_by=None, modified_by=None, tenant_id=None, acl=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowCompact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._href = None
        self._name = None
        self._organization = None
        self._description = None
        self._category = None
        self._tool_class = None
        self._time_created = None
        self._time_modified = None
        self._created_by = None
        self._modified_by = None
        self._tenant_id = None
        self._acl = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if tool_class is not None:
            self.tool_class = tool_class
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if acl is not None:
            self.acl = acl

    @property
    def id(self):
        """Gets the id of this WorkflowCompact.  # noqa: E501

        Unique resource ID  # noqa: E501

        :return: The id of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkflowCompact.

        Unique resource ID  # noqa: E501

        :param id: The id of this WorkflowCompact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this WorkflowCompact.  # noqa: E501

        HREF to the resource  # noqa: E501

        :return: The href of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this WorkflowCompact.

        HREF to the resource  # noqa: E501

        :param href: The href of this WorkflowCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this WorkflowCompact.  # noqa: E501

        Name of the workflow  # noqa: E501

        :return: The name of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowCompact.

        Name of the workflow  # noqa: E501

        :param name: The name of this WorkflowCompact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this WorkflowCompact.  # noqa: E501

        Organization associated with the workflow  # noqa: E501

        :return: The organization of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this WorkflowCompact.

        Organization associated with the workflow  # noqa: E501

        :param organization: The organization of this WorkflowCompact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                organization is not None and len(organization) > 255):
            raise ValueError("Invalid value for `organization`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                organization is not None and len(organization) < 0):
            raise ValueError("Invalid value for `organization`, length must be greater than or equal to `0`")  # noqa: E501

        self._organization = organization

    @property
    def description(self):
        """Gets the description of this WorkflowCompact.  # noqa: E501

        Description of the workflow  # noqa: E501

        :return: The description of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowCompact.

        Description of the workflow  # noqa: E501

        :param description: The description of this WorkflowCompact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 128):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def category(self):
        """Gets the category of this WorkflowCompact.  # noqa: E501

        Category of the workflow  # noqa: E501

        :return: The category of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this WorkflowCompact.

        Category of the workflow  # noqa: E501

        :param category: The category of this WorkflowCompact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) > 128):
            raise ValueError("Invalid value for `category`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) < 0):
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `0`")  # noqa: E501

        self._category = category

    @property
    def tool_class(self):
        """Gets the tool_class of this WorkflowCompact.  # noqa: E501

        Workflow type  # noqa: E501

        :return: The tool_class of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._tool_class

    @tool_class.setter
    def tool_class(self, tool_class):
        """Sets the tool_class of this WorkflowCompact.

        Workflow type  # noqa: E501

        :param tool_class: The tool_class of this WorkflowCompact.  # noqa: E501
        :type: str
        """

        self._tool_class = tool_class

    @property
    def time_created(self):
        """Gets the time_created of this WorkflowCompact.  # noqa: E501

        Time (in UTC) the resource was created  # noqa: E501

        :return: The time_created of this WorkflowCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this WorkflowCompact.

        Time (in UTC) the resource was created  # noqa: E501

        :param time_created: The time_created of this WorkflowCompact.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def time_modified(self):
        """Gets the time_modified of this WorkflowCompact.  # noqa: E501

        Time (in UTC) the resource was modified  # noqa: E501

        :return: The time_modified of this WorkflowCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this WorkflowCompact.

        Time (in UTC) the resource was modified  # noqa: E501

        :param time_modified: The time_modified of this WorkflowCompact.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def created_by(self):
        """Gets the created_by of this WorkflowCompact.  # noqa: E501

        User that created the resource  # noqa: E501

        :return: The created_by of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkflowCompact.

        User that created the resource  # noqa: E501

        :param created_by: The created_by of this WorkflowCompact.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_by(self):
        """Gets the modified_by of this WorkflowCompact.  # noqa: E501

        User that modified the resource  # noqa: E501

        :return: The modified_by of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this WorkflowCompact.

        User that modified the resource  # noqa: E501

        :param modified_by: The modified_by of this WorkflowCompact.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def tenant_id(self):
        """Gets the tenant_id of this WorkflowCompact.  # noqa: E501

        Tenant ID the resource belongs to  # noqa: E501

        :return: The tenant_id of this WorkflowCompact.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this WorkflowCompact.

        Tenant ID the resource belongs to  # noqa: E501

        :param tenant_id: The tenant_id of this WorkflowCompact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) > 255):
            raise ValueError("Invalid value for `tenant_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) < 0):
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def acl(self):
        """Gets the acl of this WorkflowCompact.  # noqa: E501

        Access control list of the resource  # noqa: E501

        :return: The acl of this WorkflowCompact.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this WorkflowCompact.

        Access control list of the resource  # noqa: E501

        :param acl: The acl of this WorkflowCompact.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

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
        if not isinstance(other, WorkflowCompact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowCompact):
            return True

        return self.to_dict() != other.to_dict()
