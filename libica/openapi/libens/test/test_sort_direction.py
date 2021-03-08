# coding: utf-8

"""
    Event Notification Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libica.openapi.libens
from libica.openapi.libens.models.sort_direction import SortDirection  # noqa: E501
from libica.openapi.libens.rest import ApiException

class TestSortDirection(unittest.TestCase):
    """SortDirection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SortDirection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libens.models.sort_direction.SortDirection()  # noqa: E501
        if include_optional :
            return SortDirection(
            )
        else :
            return SortDirection(
        )

    def testSortDirection(self):
        """Test SortDirection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()