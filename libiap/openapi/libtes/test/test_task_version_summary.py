# coding: utf-8

"""
    Task Execution Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libiap.openapi.libtes
from libiap.openapi.libtes.models.task_version_summary import TaskVersionSummary  # noqa: E501
from libiap.openapi.libtes.rest import ApiException

class TestTaskVersionSummary(unittest.TestCase):
    """TaskVersionSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskVersionSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libtes.models.task_version_summary.TaskVersionSummary()  # noqa: E501
        if include_optional :
            return TaskVersionSummary(
                id = '0', 
                href = '0', 
                version = '0', 
                description = '0', 
                acl = [
                    '0'
                    ], 
                tenant_id = '0', 
                sub_tenant_id = '0', 
                created_by = '0', 
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_by = '0', 
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return TaskVersionSummary(
        )

    def testTaskVersionSummary(self):
        """Test TaskVersionSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
