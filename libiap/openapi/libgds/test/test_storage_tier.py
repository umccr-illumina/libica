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
from libiap.openapi.libgds.models.storage_tier import StorageTier  # noqa: E501
from libiap.openapi.libgds.rest import ApiException

class TestStorageTier(unittest.TestCase):
    """StorageTier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StorageTier
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libgds.models.storage_tier.StorageTier()  # noqa: E501
        if include_optional :
            return StorageTier(
            )
        else :
            return StorageTier(
        )

    def testStorageTier(self):
        """Test StorageTier"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
