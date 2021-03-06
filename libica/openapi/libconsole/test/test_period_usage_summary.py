# coding: utf-8

"""
    Developer Console Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import libica.openapi.libconsole
from libica.openapi.libconsole.models.period_usage_summary import PeriodUsageSummary  # noqa: E501
from libica.openapi.libconsole.rest import ApiException

class TestPeriodUsageSummary(unittest.TestCase):
    """PeriodUsageSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PeriodUsageSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libconsole.models.period_usage_summary.PeriodUsageSummary()  # noqa: E501
        if include_optional :
            return PeriodUsageSummary(
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                i_credit = 56, 
                total_usages = [
                    libica.openapi.libconsole.models.product_usage.ProductUsage(
                        type = '0', 
                        amount = 1.337, 
                        unit = '0', 
                        i_credit = 1.337, )
                    ], 
                user_aggregated_usages = [
                    libica.openapi.libconsole.models.user_aggregated_usage.UserAggregatedUsage(
                        user = libica.openapi.libconsole.models.user.User(
                            full_name = '0', 
                            user_name = '0', 
                            domain = libica.openapi.libconsole.models.domain.Domain(
                                id = '0', 
                                name = '0', ), 
                            type = '0', ), 
                        i_credit = 1.337, 
                        usages = [
                            libica.openapi.libconsole.models.product_usage.ProductUsage(
                                type = '0', 
                                amount = 1.337, 
                                unit = '0', 
                                i_credit = 1.337, )
                            ], )
                    ]
            )
        else :
            return PeriodUsageSummary(
        )

    def testPeriodUsageSummary(self):
        """Test PeriodUsageSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
