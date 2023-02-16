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
from libica.openapi.libtes.models.cluster import Cluster  # noqa: E501
from libica.openapi.libtes.rest import ApiException

class TestCluster(unittest.TestCase):
    """Cluster unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Cluster
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = libica.openapi.libtes.models.cluster.Cluster()  # noqa: E501
        if include_optional :
            return Cluster(
                id = '0', 
                href = '0', 
                urn = '0', 
                name = '0', 
                svc_acct_u_id = '0', 
                status = '0', 
                type = '0', 
                task_runs = [
                    libica.openapi.libtes.models.task_run.TaskRun(
                        id = '0', 
                        href = '0', 
                        urn = '0', 
                        name = '0', 
                        description = '0', 
                        status = 'Pending', 
                        status_details = '0', 
                        type_of_resource = '0', 
                        size_of_resource = '0', 
                        tier_of_resource = '0', 
                        execution = libica.openapi.libtes.models.execution.Execution(
                            image = libica.openapi.libtes.models.image.Image(
                                name = '0', 
                                tag = '0', 
                                digest = '0', 
                                credentials = libica.openapi.libtes.models.credentials.Credentials(
                                    username = '0', 
                                    password = '0', ), ), 
                            command = '0', 
                            args = [
                                '0'
                                ], 
                            inputs = [
                                libica.openapi.libtes.models.input_mount_mapping_with_creds.InputMountMappingWithCreds(
                                    storage_provider = '0', 
                                    path = '0', 
                                    url = '0', 
                                    urn = '0', 
                                    mode = '0', 
                                    type = 'File', )
                                ], 
                            outputs = [
                                libica.openapi.libtes.models.mount_mapping_with_creds.MountMappingWithCreds(
                                    path = '0', 
                                    url = '0', 
                                    urn = '0', 
                                    type = '0', 
                                    storage_provider = '0', 
                                    service_url = '0', )
                                ], 
                            system_files = libica.openapi.libtes.models.system_files.SystemFiles(
                                url = '0', 
                                urn = '0', 
                                storage_provider = '0', ), 
                            environment = libica.openapi.libtes.models.environment.Environment(
                                variables = {
                                    'key' : '0'
                                    }, 
                                resources = libica.openapi.libtes.models.resources.Resources(
                                    type = '0', 
                                    size = '0', 
                                    cpu_cores = 1.337, 
                                    memory_gb = 1.337, 
                                    hardware = [
                                        '0'
                                        ], 
                                    tier = '0', ), 
                                input_stream_settings = libica.openapi.libtes.models.input_stream_settings.InputStreamSettings(
                                    access_pattern = 'sequential', 
                                    cache_size_gb = 5E+1, 
                                    block_size_mb = 0, 
                                    prefetch_blocks = 0, ), ), 
                            working_directory = '0', 
                            retry_limit = 56, 
                            retry_count = 56, ), 
                        task_version_summary = libica.openapi.libtes.models.task_version_summary.TaskVersionSummary(
                            id = '0', 
                            href = '0', 
                            urn = '0', 
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
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        logs = [
                            libica.openapi.libtes.models.task_run_logs.TaskRunLogs(
                                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                error = '0', 
                                error_details = '0', 
                                stdout = '0', 
                                stderr = '0', )
                            ], 
                        execution_raw_json = '0', 
                        acl = [
                            '0'
                            ], 
                        tenant_id = '0', 
                        sub_tenant_id = '0', 
                        created_by = '0', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_by = '0', 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
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
            return Cluster(
        )

    def testCluster(self):
        """Test Cluster"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
