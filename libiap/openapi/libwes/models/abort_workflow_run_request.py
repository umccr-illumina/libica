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


class AbortWorkflowRunRequest(object):
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
        'error': 'str',
        'cause': 'str'
    }

    attribute_map = {
        'error': 'error',
        'cause': 'cause'
    }

    def __init__(self, error=None, cause=None, local_vars_configuration=None):  # noqa: E501
        """AbortWorkflowRunRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._cause = None
        self.discriminator = None

        self.error = error
        if cause is not None:
            self.cause = cause

    @property
    def error(self):
        """Gets the error of this AbortWorkflowRunRequest.  # noqa: E501


        :return: The error of this AbortWorkflowRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AbortWorkflowRunRequest.


        :param error: The error of this AbortWorkflowRunRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error is None:  # noqa: E501
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                error is not None and len(error) > 256):
            raise ValueError("Invalid value for `error`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                error is not None and len(error) < 0):
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `0`")  # noqa: E501

        self._error = error

    @property
    def cause(self):
        """Gets the cause of this AbortWorkflowRunRequest.  # noqa: E501


        :return: The cause of this AbortWorkflowRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this AbortWorkflowRunRequest.


        :param cause: The cause of this AbortWorkflowRunRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cause is not None and len(cause) > 32768):
            raise ValueError("Invalid value for `cause`, length must be less than or equal to `32768`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cause is not None and len(cause) < 0):
            raise ValueError("Invalid value for `cause`, length must be greater than or equal to `0`")  # noqa: E501

        self._cause = cause

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
        if not isinstance(other, AbortWorkflowRunRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AbortWorkflowRunRequest):
            return True

        return self.to_dict() != other.to_dict()
