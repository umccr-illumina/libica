# coding: utf-8

"""
    Genomic Data Store Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libica.openapi.libgds
from libica.openapi.libgds.models.object_container_settings import ObjectContainerSettings  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestObjectContainerSettings(unittest.TestCase):
    """ObjectContainerSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ObjectContainerSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.object_container_settings.ObjectContainerSettings()  # noqa: E501
        if include_optional :
            return ObjectContainerSettings(
                object_container = '012', 
                key_prefix = 'a', 
                server_side_encryption_algorithm = '0', 
                server_side_encryption_key = '0'
            )
        else :
            return ObjectContainerSettings(
                object_container = '012',
        )

    def testObjectContainerSettings(self):
        """Test ObjectContainerSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()