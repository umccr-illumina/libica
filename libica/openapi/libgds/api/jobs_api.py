# coding: utf-8

"""
    Genomic Data Store Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from libica.openapi.libgds.api_client import ApiClient
from libica.openapi.libgds.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class JobsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def abort_job(self, job_id, **kwargs):  # noqa: E501
        """Abort a job in GDS.  # noqa: E501

        Abort the specified job ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.abort_job(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str job_id: Unique identifier for the job to be aborted. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.abort_job_with_http_info(job_id, **kwargs)  # noqa: E501

    def abort_job_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Abort a job in GDS.  # noqa: E501

        Abort the specified job ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.abort_job_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str job_id: Unique identifier for the job to be aborted. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(JobResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'job_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method abort_job" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'job_id' is set
        if self.api_client.client_side_validation and ('job_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_id` when calling `abort_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['jobId'] = local_var_params['job_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/jobs/{jobId}:abort', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_job(self, job_id, **kwargs):  # noqa: E501
        """Get information about a job in GDS.  # noqa: E501

        Get information for the specified job ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str job_id: Unique identifier for the job to retrieve. (required)
        :param str tenant_id: Optional parameter to see shared data in another tenant
        :param bool include_errors:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_job_with_http_info(job_id, **kwargs)  # noqa: E501

    def get_job_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Get information about a job in GDS.  # noqa: E501

        Get information for the specified job ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_job_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str job_id: Unique identifier for the job to retrieve. (required)
        :param str tenant_id: Optional parameter to see shared data in another tenant
        :param bool include_errors:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(JobResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'job_id',
            'tenant_id',
            'include_errors'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_job" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'job_id' is set
        if self.api_client.client_side_validation and ('job_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['job_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job_id` when calling `get_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['jobId'] = local_var_params['job_id']  # noqa: E501

        query_params = []
        if 'tenant_id' in local_var_params and local_var_params['tenant_id'] is not None:  # noqa: E501
            query_params.append(('tenantId', local_var_params['tenant_id']))  # noqa: E501
        if 'include_errors' in local_var_params and local_var_params['include_errors'] is not None:  # noqa: E501
            query_params.append(('includeErrors', local_var_params['include_errors']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/jobs/{jobId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_jobs(self, folder_id, **kwargs):  # noqa: E501
        """Get a list of jobs for a given folder  # noqa: E501

        Given a folder id, get a list of jobs accessible by the JWT. The default sort returned is by job progress status. The default page size is 10 items  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_jobs(folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str folder_id: (required)
        :param str job_statuses: Optional field that specifies comma-separated JobStatuses to include in the list
        :param int page_size: START_DESC END_DESC
        :param str page_token: START_DESC END_DESC
        :param str include: Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: JobListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_jobs_with_http_info(folder_id, **kwargs)  # noqa: E501

    def list_jobs_with_http_info(self, folder_id, **kwargs):  # noqa: E501
        """Get a list of jobs for a given folder  # noqa: E501

        Given a folder id, get a list of jobs accessible by the JWT. The default sort returned is by job progress status. The default page size is 10 items  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_jobs_with_http_info(folder_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str folder_id: (required)
        :param str job_statuses: Optional field that specifies comma-separated JobStatuses to include in the list
        :param int page_size: START_DESC END_DESC
        :param str page_token: START_DESC END_DESC
        :param str include: Optionally include additional fields in the response. Multiple fields can be included by comma-separation.  Possible values: TotalItemCount, InheritedAcl
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(JobListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'folder_id',
            'job_statuses',
            'page_size',
            'page_token',
            'include'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_jobs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'folder_id' is set
        if self.api_client.client_side_validation and ('folder_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['folder_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `folder_id` when calling `list_jobs`")  # noqa: E501

        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_jobs`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_jobs`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_statuses' in local_var_params and local_var_params['job_statuses'] is not None:  # noqa: E501
            query_params.append(('jobStatuses', local_var_params['job_statuses']))  # noqa: E501
        if 'folder_id' in local_var_params and local_var_params['folder_id'] is not None:  # noqa: E501
            query_params.append(('folderId', local_var_params['folder_id']))  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'page_token' in local_var_params and local_var_params['page_token'] is not None:  # noqa: E501
            query_params.append(('pageToken', local_var_params['page_token']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
