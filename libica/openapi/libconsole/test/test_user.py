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

import libica.openapi.libconsole
from libica.openapi.libconsole.models.user import User  # noqa: E501
from libica.openapi.libconsole.rest import ApiException

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libconsole.models.user.User()  # noqa: E501
        if include_optional :
            return User(
                full_name = '0', 
                user_name = '0', 
                domain = libica.openapi.libconsole.models.domain.Domain(
                    id = '0', 
                    name = '0', ), 
                type = '0'
            )
        else :
            return User(
        )

    def testUser(self):
        """Test User"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()