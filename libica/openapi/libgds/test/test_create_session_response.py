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
from libica.openapi.libgds.models.create_session_response import CreateSessionResponse  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestCreateSessionResponse(unittest.TestCase):
    """CreateSessionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateSessionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.create_session_response.CreateSessionResponse()  # noqa: E501
        if include_optional :
            return CreateSessionResponse(
                object_store_access = libica.openapi.libgds.models.object_store_access.ObjectStoreAccess(
                    session_id = '0', 
                    aws_s3_temporary_upload_credentials = libica.openapi.libgds.models.aws_s3_temporary_upload_credentials.AwsS3TemporaryUploadCredentials(
                        access_key_id = '0', 
                        secret_access_key = '0', 
                        session_token = '0', 
                        region = '0', 
                        bucket_name = '0', 
                        key_prefix = '0', 
                        expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        service_url = '0', 
                        server_side_encryption_algorithm = '0', 
                        server_side_encryption_key = '0', ), 
                    aws_s3_presigned_url_for_upload = libica.openapi.libgds.models.aws_s3_presigned_url_for_upload.AwsS3PresignedUrlForUpload(
                        single_part_url = '0', 
                        multipart_template = '0', 
                        multipart_signatures = [
                            libica.openapi.libgds.models.part_info.PartInfo(
                                part = 56, 
                                date = '0', 
                                date_time = '0', 
                                signature = '0', )
                            ], 
                        multipart_upload_id = '0', 
                        server_side_encryption_algorithm = '0', 
                        server_side_encryption_key = '0', ), ), 
                id = '0', 
                folder_urn = '0', 
                status = 'Open', 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_credentials_expire = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_closed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                time_completed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                metadata = None
            )
        else :
            return CreateSessionResponse(
        )

    def testCreateSessionResponse(self):
        """Test CreateSessionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
