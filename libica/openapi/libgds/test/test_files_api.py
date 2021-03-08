# coding: utf-8

"""
    Genomic Data Store Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import libica.openapi.libgds
from libica.openapi.libgds.api.files_api import FilesApi  # noqa: E501
from libica.openapi.libgds.rest import ApiException


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = libica.openapi.libgds.api.files_api.FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_archive_file(self):
        """Test case for archive_file

        Archive a file  # noqa: E501
        """
        pass

    def test_create_file(self):
        """Test case for create_file

        Create a file entry in GDS and get temporary credentials for upload  # noqa: E501
        """
        pass

    def test_delete_file(self):
        """Test case for delete_file

        Permanently delete a file  # noqa: E501
        """
        pass

    def test_get_file(self):
        """Test case for get_file

        Get details about a file, including a pre-signed URL for download  # noqa: E501
        """
        pass

    def test_list_files(self):
        """Test case for list_files

        Get a list of files  # noqa: E501
        """
        pass

    def test_unarchive_file(self):
        """Test case for unarchive_file

        Unarchive a file  # noqa: E501
        """
        pass

    def test_update_file(self):
        """Test case for update_file

        Update a file entry in GDS and get temporary credentials for upload  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()