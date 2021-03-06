# coding: utf-8

"""
    Developer Console Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import libica.openapi.libconsole
from libica.openapi.libconsole.api.health_api import HealthApi  # noqa: E501
from libica.openapi.libconsole.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = libica.openapi.libconsole.api.health_api.HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_service_health(self):
        """Test case for service_health

        Returns the health status for all services.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
