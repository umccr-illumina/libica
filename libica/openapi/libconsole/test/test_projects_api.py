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
from libica.openapi.libconsole.api.projects_api import ProjectsApi  # noqa: E501
from libica.openapi.libconsole.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = libica.openapi.libconsole.api.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_projects(self):
        """Test case for list_projects

        Get a list of available projects. Requires user authorization Bearer token.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()