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

import libiap.openapi.libens
from libiap.openapi.libens.models.subscription_list import SubscriptionList  # noqa: E501
from libiap.openapi.libens.rest import ApiException

class TestSubscriptionList(unittest.TestCase):
    """SubscriptionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libiap.openapi.libens.models.subscription_list.SubscriptionList()  # noqa: E501
        if include_optional :
            return SubscriptionList(
                items = [
                    libiap.openapi.libens.models.subscription.Subscription(
                        id = '0', 
                        urn = '0', 
                        type = '0', 
                        actions = [
                            '0'
                            ], 
                        filter_expression = '0', 
                        name = '0', 
                        description = '0', 
                        delivery_target = libiap.openapi.libens.models.delivery_target.DeliveryTarget(
                            aws_sns_topic = libiap.openapi.libens.models.delivery_target_aws_sns_topic.DeliveryTargetAwsSnsTopic(
                                topic_arn = '0', ), 
                            aws_sqs_queue = libiap.openapi.libens.models.delivery_target_aws_sqs_queue.DeliveryTargetAwsSqsQueue(
                                queue_url = '0', ), 
                            workflow_run_launch = libiap.openapi.libens.models.delivery_target_workflow_run_launch.DeliveryTargetWorkflowRunLaunch(
                                id = '0', 
                                version = '0', 
                                name = '0', 
                                # input = libiap.openapi.libens.models.input.input(),
                            ),
                        ),
                        tenant_id = '0', 
                        created_by_user_id = '0', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deleted_by_user_id = '0', 
                        time_deleted = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_deleted = True, )
                    ], 
                item_count = 56, 
                first_page_token = '0', 
                next_page_token = '0', 
                prev_page_token = '0', 
                last_page_token = '0', 
                total_item_count = 56, 
                total_page_count = 56, 
                sorted_by = 'id', 
                sort_direction = 'Asc'
            )
        else :
            return SubscriptionList(
        )

    def testSubscriptionList(self):
        """Test SubscriptionList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()