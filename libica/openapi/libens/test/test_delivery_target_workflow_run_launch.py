# coding: utf-8

"""
    Event Notification Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libica.openapi.libens
from libica.openapi.libens.models.delivery_target_workflow_run_launch import DeliveryTargetWorkflowRunLaunch  # noqa: E501
from libica.openapi.libens.rest import ApiException

class TestDeliveryTargetWorkflowRunLaunch(unittest.TestCase):
    """DeliveryTargetWorkflowRunLaunch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeliveryTargetWorkflowRunLaunch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libens.models.delivery_target_workflow_run_launch.DeliveryTargetWorkflowRunLaunch()  # noqa: E501
        if include_optional :
            return DeliveryTargetWorkflowRunLaunch(
                id = '0', 
                version = '0', 
                name = '0', 
                input = None
            )
        else :
            return DeliveryTargetWorkflowRunLaunch(
                id = '0',
                version = '0',
                name = '0',
        )

    def testDeliveryTargetWorkflowRunLaunch(self):
        """Test DeliveryTargetWorkflowRunLaunch"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
