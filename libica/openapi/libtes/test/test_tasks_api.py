# coding: utf-8

"""
    Task Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import libica.openapi.libtes
from libica.openapi.libtes.api.tasks_api import TasksApi  # noqa: E501
from libica.openapi.libtes.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = libica.openapi.libtes.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_task(self):
        """Test case for create_task

        Create a Task  # noqa: E501
        """
        pass

    def test_get_task(self):
        """Test case for get_task

        Get the details of a Task  # noqa: E501
        """
        pass

    def test_list_tasks(self):
        """Test case for list_tasks

        Get a list of tasks  # noqa: E501
        """
        pass

    def test_update_task(self):
        """Test case for update_task

        Update an existing task.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
