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
from libica.openapi.libtes.api.task_runs_api import TaskRunsApi  # noqa: E501
from libica.openapi.libtes.rest import ApiException


class TestTaskRunsApi(unittest.TestCase):
    """TaskRunsApi unit test stubs"""

    def setUp(self):
        self.api = libica.openapi.libtes.api.task_runs_api.TaskRunsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abort_task_run(self):
        """Test case for abort_task_run

        Abort a task run  # noqa: E501
        """
        pass

    def test_create_task_run(self):
        """Test case for create_task_run

        Create and launch a task run  # noqa: E501
        """
        pass

    def test_get_task_run(self):
        """Test case for get_task_run

        Get the status of a task run  # noqa: E501
        """
        pass

    def test_list_task_runs(self):
        """Test case for list_task_runs

        Get a list of task runs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()