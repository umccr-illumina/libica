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
from libica.openapi.libgds.models.bulk_metadata_update_operation_parameters import BulkMetadataUpdateOperationParameters  # noqa: E501
from libica.openapi.libgds.rest import ApiException

class TestBulkMetadataUpdateOperationParameters(unittest.TestCase):
    """BulkMetadataUpdateOperationParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BulkMetadataUpdateOperationParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libgds.models.bulk_metadata_update_operation_parameters.BulkMetadataUpdateOperationParameters()  # noqa: E501
        if include_optional :
            # FIXME updateMetadata and deleteMetadata is just string
            return BulkMetadataUpdateOperationParameters(
                folder_id = '0', 
                folder_path = '0', 
                volume_id = '0', 
                file_status = '0', 
                parent_folder_metadata_updates = libica.openapi.libgds.models.metadata_update_request.MetadataUpdateRequest(
                    update_metadata = "",
                    delete_metadata = "", ),
                children_folders_updates = libica.openapi.libgds.models.metadata_update_request.MetadataUpdateRequest(
                    update_metadata = "",
                    delete_metadata = "", ),
                children_files_updates = libica.openapi.libgds.models.metadata_update_request.MetadataUpdateRequest(
                    update_metadata = "",
                    delete_metadata = "", )
            )
        else :
            return BulkMetadataUpdateOperationParameters(
        )

    def testBulkMetadataUpdateOperationParameters(self):
        """Test BulkMetadataUpdateOperationParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
