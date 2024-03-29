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
from libica.openapi.libgds.models.aws_s3_temporary_read_only_credentials import AwsS3TemporaryReadOnlyCredentials  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestAwsS3TemporaryReadOnlyCredentials(unittest.TestCase):
    """AwsS3TemporaryReadOnlyCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsS3TemporaryReadOnlyCredentials
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.aws_s3_temporary_read_only_credentials.AwsS3TemporaryReadOnlyCredentials()  # noqa: E501
        if include_optional :
            return AwsS3TemporaryReadOnlyCredentials(
                access_key_id = '0', 
                secret_access_key = '0', 
                session_token = '0', 
                region = '0', 
                bucket_name = '0', 
                key_prefix = '0', 
                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                service_url = '0', 
                server_side_encryption_algorithm = '0', 
                server_side_encryption_key = '0'
            )
        else :
            return AwsS3TemporaryReadOnlyCredentials(
        )

    def testAwsS3TemporaryReadOnlyCredentials(self):
        """Test AwsS3TemporaryReadOnlyCredentials"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
