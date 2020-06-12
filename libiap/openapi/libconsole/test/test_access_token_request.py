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
from libiap.openapi.libconsole.models.access_token_request import AccessTokenRequest  # noqa: E501
from libiap.openapi.libconsole.rest import ApiException

class TestAccessTokenRequest(unittest.TestCase):
    """AccessTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccessTokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libconsole.models.access_token_request.AccessTokenRequest()  # noqa: E501
        if include_optional :
            return AccessTokenRequest(
                access_token = '0'
            )
        else :
            return AccessTokenRequest(
        )

    def testAccessTokenRequest(self):
        """Test AccessTokenRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
