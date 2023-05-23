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
from libica.openapi.libgds.models.volume_configuration_response import VolumeConfigurationResponse  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestVolumeConfigurationResponse(unittest.TestCase):
    """VolumeConfigurationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VolumeConfigurationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.volume_configuration_response.VolumeConfigurationResponse()  # noqa: E501
        if include_optional :
            return VolumeConfigurationResponse(
                name = '0', 
                tenant_id = '0', 
                sub_tenant_id = '0', 
                urn = '0', 
                online_status = 'Initializing', 
                error_code = '0', 
                error_message = '0', 
                time_of_last_error = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_by = '0', 
                object_store_settings = libica.openapi.libgds.models.object_store_settings.ObjectStoreSettings(
                    aws_s3 = libica.openapi.libgds.models.awss3_object_store_setting.AWSS3ObjectStoreSetting(
                        bucket_name = '012', 
                        key_prefix = 'gds-volumes/', ), 
                    # platform_credentials_name = '0',
                    secret_name='test',  # pragma: allowlist secret
                )
            )
        else :
            return VolumeConfigurationResponse(
        )

    def testVolumeConfigurationResponse(self):
        """Test VolumeConfigurationResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
