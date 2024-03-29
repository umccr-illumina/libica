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
from libica.openapi.libgds.api.jobs_api import JobsApi  # noqa: E501
from libica.openapi.libgds.rest import ApiException


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = libica.openapi.libgds.api.jobs_api.JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abort_job(self):
        """Test case for abort_job

        Abort a job in GDS.  # noqa: E501
        """
        pass

    def test_get_job(self):
        """Test case for get_job

        Get information about a job in GDS.  # noqa: E501
        """
        pass

    def test_list_jobs(self):
        """Test case for list_jobs

        Get a list of jobs for a given folder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
