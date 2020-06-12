# coding: utf-8

"""
    Developer Console Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libiap.openapi.libconsole
from libiap.openapi.libconsole.models.workgroup import Workgroup  # noqa: E501
from libiap.openapi.libconsole.rest import ApiException

class TestWorkgroup(unittest.TestCase):
    """Workgroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Workgroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libconsole.models.workgroup.Workgroup()  # noqa: E501
        if include_optional :
            return Workgroup(
                id = '0', 
                name = '0', 
                description = '0'
            )
        else :
            return Workgroup(
        )

    def testWorkgroup(self):
        """Test Workgroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()