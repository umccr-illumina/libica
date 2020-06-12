# coding: utf-8

"""
    Workflow Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libiap.openapi.libwes
from libiap.openapi.libwes.models.get_workflow_run_include_flags import GetWorkflowRunIncludeFlags  # noqa: E501
from libiap.openapi.libwes.rest import ApiException

class TestGetWorkflowRunIncludeFlags(unittest.TestCase):
    """GetWorkflowRunIncludeFlags unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetWorkflowRunIncludeFlags
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libwes.models.get_workflow_run_include_flags.GetWorkflowRunIncludeFlags()  # noqa: E501
        if include_optional :
            return GetWorkflowRunIncludeFlags(
            )
        else :
            return GetWorkflowRunIncludeFlags(
        )

    def testGetWorkflowRunIncludeFlags(self):
        """Test GetWorkflowRunIncludeFlags"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
