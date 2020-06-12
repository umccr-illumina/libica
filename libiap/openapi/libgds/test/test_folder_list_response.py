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

import libiap.openapi.libgds
from libiap.openapi.libgds.models.folder_list_response import FolderListResponse  # noqa: E501
from libiap.openapi.libgds.rest import ApiException

class TestFolderListResponse(unittest.TestCase):
    """FolderListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FolderListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libgds.models.folder_list_response.FolderListResponse()  # noqa: E501
        if include_optional :
            return FolderListResponse(
                items = [
                    libiap.openapi.libgds.models.folder_response.FolderResponse(
                        id = '0', 
                        name = '0', 
                        volume_id = '0', 
                        volume_name = '0', 
                        tenant_id = '0', 
                        sub_tenant_id = '0', 
                        urn = '0', 
                        path = '0', 
                        acl = [
                            '0'
                            ], 
                        inherited_acl = [
                            '0'
                            ], 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by = '0', 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_by = '0', 
                        job_status = 'None', 
                        archive_job_storage_tier = 'None', )
                    ], 
                item_count = 56, 
                first_page_token = '0', 
                next_page_token = '0', 
                prev_page_token = '0', 
                last_page_token = '0', 
                total_item_count = 56, 
                total_page_count = 56
            )
        else :
            return FolderListResponse(
        )

    def testFolderListResponse(self):
        """Test FolderListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
