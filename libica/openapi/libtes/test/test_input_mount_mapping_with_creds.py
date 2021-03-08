# coding: utf-8

"""
    Task Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libica.openapi.libtes
from libica.openapi.libtes.models.input_mount_mapping_with_creds import InputMountMappingWithCreds  # noqa: E501
from libica.openapi.libtes.rest import ApiException

class TestInputMountMappingWithCreds(unittest.TestCase):
    """InputMountMappingWithCreds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InputMountMappingWithCreds
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libtes.models.input_mount_mapping_with_creds.InputMountMappingWithCreds()  # noqa: E501
        if include_optional :
            return InputMountMappingWithCreds(
                storage_provider = '0', 
                credentials = {
                    'key' : '0'
                    }, 
                path = '0', 
                url = '0', 
                urn = '0', 
                mode = '0', 
                type = 'File'
            )
        else :
            return InputMountMappingWithCreds(
        )

    def testInputMountMappingWithCreds(self):
        """Test InputMountMappingWithCreds"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()