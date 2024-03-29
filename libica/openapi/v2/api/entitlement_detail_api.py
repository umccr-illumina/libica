"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p>   # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from libica.openapi.v2.api_client import ApiClient, Endpoint as _Endpoint
from libica.openapi.v2.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from libica.openapi.v2.model.activation_code_detail import ActivationCodeDetail
from libica.openapi.v2.model.activation_code_detail_list import ActivationCodeDetailList
from libica.openapi.v2.model.problem import Problem
from libica.openapi.v2.model.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
from libica.openapi.v2.model.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis


class EntitlementDetailApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.find_all_matching_activation_codes_for_cwl_endpoint = _Endpoint(
            settings={
                'response_type': (ActivationCodeDetailList,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/activationCodes:findAllMatchingForCwl',
                'operation_id': 'find_all_matching_activation_codes_for_cwl',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'search_matching_activation_codes_for_cwl_analysis',
                ],
                'required': [
                    'search_matching_activation_codes_for_cwl_analysis',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search_matching_activation_codes_for_cwl_analysis':
                        (SearchMatchingActivationCodesForCwlAnalysis,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'search_matching_activation_codes_for_cwl_analysis': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/vnd.illumina.v3+json'
                ],
                'content_type': [
                    'application/vnd.illumina.v3+json',
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.find_all_matching_activation_codes_for_nextflow_endpoint = _Endpoint(
            settings={
                'response_type': (ActivationCodeDetailList,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/activationCodes:findAllMatchingForNextflow',
                'operation_id': 'find_all_matching_activation_codes_for_nextflow',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'search_matching_activation_codes_for_nextflow_analysis',
                ],
                'required': [
                    'search_matching_activation_codes_for_nextflow_analysis',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search_matching_activation_codes_for_nextflow_analysis':
                        (SearchMatchingActivationCodesForNextflowAnalysis,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'search_matching_activation_codes_for_nextflow_analysis': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/vnd.illumina.v3+json'
                ],
                'content_type': [
                    'application/vnd.illumina.v3+json',
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.find_best_matching_activation_code_for_cwl_endpoint = _Endpoint(
            settings={
                'response_type': (ActivationCodeDetail,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/activationCodes:findBestMatchingForCwl',
                'operation_id': 'find_best_matching_activation_code_for_cwl',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'search_matching_activation_codes_for_cwl_analysis',
                ],
                'required': [
                    'search_matching_activation_codes_for_cwl_analysis',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search_matching_activation_codes_for_cwl_analysis':
                        (SearchMatchingActivationCodesForCwlAnalysis,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'search_matching_activation_codes_for_cwl_analysis': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/vnd.illumina.v3+json'
                ],
                'content_type': [
                    'application/vnd.illumina.v3+json',
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.find_best_matching_activation_codes_for_nextflow_endpoint = _Endpoint(
            settings={
                'response_type': (ActivationCodeDetail,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/activationCodes:findBestMatchingForNextflow',
                'operation_id': 'find_best_matching_activation_codes_for_nextflow',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'search_matching_activation_codes_for_nextflow_analysis',
                ],
                'required': [
                    'search_matching_activation_codes_for_nextflow_analysis',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search_matching_activation_codes_for_nextflow_analysis':
                        (SearchMatchingActivationCodesForNextflowAnalysis,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'search_matching_activation_codes_for_nextflow_analysis': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/vnd.illumina.v3+json'
                ],
                'content_type': [
                    'application/vnd.illumina.v3+json',
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def find_all_matching_activation_codes_for_cwl(
        self,
        search_matching_activation_codes_for_cwl_analysis,
        **kwargs
    ):
        """Search all matching activation code details for a Cwl pipeline.  # noqa: E501

        Endpoint for searching all matching activation code details for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_all_matching_activation_codes_for_cwl(search_matching_activation_codes_for_cwl_analysis, async_req=True)
        >>> result = thread.get()

        Args:
            search_matching_activation_codes_for_cwl_analysis (SearchMatchingActivationCodesForCwlAnalysis):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ActivationCodeDetailList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search_matching_activation_codes_for_cwl_analysis'] = \
            search_matching_activation_codes_for_cwl_analysis
        return self.find_all_matching_activation_codes_for_cwl_endpoint.call_with_http_info(**kwargs)

    def find_all_matching_activation_codes_for_nextflow(
        self,
        search_matching_activation_codes_for_nextflow_analysis,
        **kwargs
    ):
        """Search all matching activation code details for a Nextflow pipeline.  # noqa: E501

        Endpoint for searching all matching activation code details for a project and an analysis from a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_all_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis, async_req=True)
        >>> result = thread.get()

        Args:
            search_matching_activation_codes_for_nextflow_analysis (SearchMatchingActivationCodesForNextflowAnalysis):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ActivationCodeDetailList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search_matching_activation_codes_for_nextflow_analysis'] = \
            search_matching_activation_codes_for_nextflow_analysis
        return self.find_all_matching_activation_codes_for_nextflow_endpoint.call_with_http_info(**kwargs)

    def find_best_matching_activation_code_for_cwl(
        self,
        search_matching_activation_codes_for_cwl_analysis,
        **kwargs
    ):
        """Search the best matching activation code detail for Cwl pipeline.  # noqa: E501

        Endpoint for searching the best activation code detail for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_best_matching_activation_code_for_cwl(search_matching_activation_codes_for_cwl_analysis, async_req=True)
        >>> result = thread.get()

        Args:
            search_matching_activation_codes_for_cwl_analysis (SearchMatchingActivationCodesForCwlAnalysis):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ActivationCodeDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search_matching_activation_codes_for_cwl_analysis'] = \
            search_matching_activation_codes_for_cwl_analysis
        return self.find_best_matching_activation_code_for_cwl_endpoint.call_with_http_info(**kwargs)

    def find_best_matching_activation_codes_for_nextflow(
        self,
        search_matching_activation_codes_for_nextflow_analysis,
        **kwargs
    ):
        """Search the best matching activation code details for Nextflow pipeline.  # noqa: E501

        Endpoint for searching the best activation code details for a project and an analysis for a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.find_best_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis, async_req=True)
        >>> result = thread.get()

        Args:
            search_matching_activation_codes_for_nextflow_analysis (SearchMatchingActivationCodesForNextflowAnalysis):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ActivationCodeDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search_matching_activation_codes_for_nextflow_analysis'] = \
            search_matching_activation_codes_for_nextflow_analysis
        return self.find_best_matching_activation_codes_for_nextflow_endpoint.call_with_http_info(**kwargs)

