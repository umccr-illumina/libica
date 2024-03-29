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

import libica.openapi.libtes
from libica.openapi.libtes.models.create_cluster_request import CreateClusterRequest  # noqa: E501
from libica.openapi.libtes.rest import ApiException

class TestCreateClusterRequest(unittest.TestCase):
    """CreateClusterRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateClusterRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libtes.models.create_cluster_request.CreateClusterRequest()  # noqa: E501
        if include_optional :
            return CreateClusterRequest(
                name = '0', 
                svc_acct_u_id = '0', 
                status = '0', 
                type = '0', 
                acl = [
                    '0'
                    ]
            )
        else :
            return CreateClusterRequest(
                name = '0',
        )

    def testCreateClusterRequest(self):
        """Test CreateClusterRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
