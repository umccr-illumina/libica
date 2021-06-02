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
from libica.openapi.libtes.models.heartbeat_task_run_request import HeartbeatTaskRunRequest  # noqa: E501
from libica.openapi.libtes.rest import ApiException

class TestHeartbeatTaskRunRequest(unittest.TestCase):
    """HeartbeatTaskRunRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HeartbeatTaskRunRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libtes.models.heartbeat_task_run_request.HeartbeatTaskRunRequest()  # noqa: E501
        if include_optional :
            return HeartbeatTaskRunRequest(
                last_heartbeat = True, 
                pod_name = '0', 
                pod_uid = '0', 
                pod_hardware_details = '0', 
                job_retry_count = 56, 
                nonce = '0', 
                container_status = [
                    libica.openapi.libtes.models.container_status.ContainerStatus(
                        name = '0', 
                        state = libica.openapi.libtes.models.container_state.ContainerState(
                            waiting = libica.openapi.libtes.models.container_state_waiting.ContainerStateWaiting(
                                reason = '0', 
                                message = '0', ), 
                            running = libica.openapi.libtes.models.container_state_running.ContainerStateRunning(
                                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            terminated = libica.openapi.libtes.models.container_state_terminated.ContainerStateTerminated(
                                exit_code = 56, 
                                signal = 56, 
                                reason = '0', 
                                message = '0', 
                                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                container_id = '0', ), ), )
                    ]
            )
        else :
            return HeartbeatTaskRunRequest(
        )

    def testHeartbeatTaskRunRequest(self):
        """Test HeartbeatTaskRunRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()