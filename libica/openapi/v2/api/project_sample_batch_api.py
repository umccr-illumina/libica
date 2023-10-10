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
from libica.openapi.v2.model.create_sample_creation_batch import CreateSampleCreationBatch
from libica.openapi.v2.model.problem import Problem
from libica.openapi.v2.model.sample_creation_batch import SampleCreationBatch
from libica.openapi.v2.model.sample_creation_batch_item_paged_list import SampleCreationBatchItemPagedList
from libica.openapi.v2.model.sample_creation_batch_sample_item import SampleCreationBatchSampleItem


class ProjectSampleBatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_sample_creation_batch_endpoint = _Endpoint(
            settings={
                'response_type': (SampleCreationBatch,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/projects/{projectId}/sampleCreationBatch',
                'operation_id': 'create_sample_creation_batch',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'create_sample_creation_batch',
                    'idempotency_key',
                ],
                'required': [
                    'project_id',
                    'create_sample_creation_batch',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'idempotency_key',
                ]
            },
            root_map={
                'validations': {
                    ('idempotency_key',): {
                        'max_length': 255,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'create_sample_creation_batch':
                        (CreateSampleCreationBatch,),
                    'idempotency_key':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'idempotency_key': 'Idempotency-Key',
                },
                'location_map': {
                    'project_id': 'path',
                    'create_sample_creation_batch': 'body',
                    'idempotency_key': 'header',
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
                    'application/x-www-form-urlencoded',
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_sample_creation_batch_endpoint = _Endpoint(
            settings={
                'response_type': (SampleCreationBatch,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/projects/{projectId}/sampleCreationBatch/{batchId}',
                'operation_id': 'get_sample_creation_batch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'batch_id',
                ],
                'required': [
                    'project_id',
                    'batch_id',
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
                    'project_id':
                        (str,),
                    'batch_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'batch_id': 'batchId',
                },
                'location_map': {
                    'project_id': 'path',
                    'batch_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/vnd.illumina.v3+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_sample_creation_batch_item_endpoint = _Endpoint(
            settings={
                'response_type': (SampleCreationBatchSampleItem,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/projects/{projectId}/sampleCreationBatch/{batchId}/items/{itemId}',
                'operation_id': 'get_sample_creation_batch_item',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'batch_id',
                    'item_id',
                ],
                'required': [
                    'project_id',
                    'batch_id',
                    'item_id',
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
                    'project_id':
                        (str,),
                    'batch_id':
                        (str,),
                    'item_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'batch_id': 'batchId',
                    'item_id': 'itemId',
                },
                'location_map': {
                    'project_id': 'path',
                    'batch_id': 'path',
                    'item_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/vnd.illumina.v3+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_sample_creation_batch_items_endpoint = _Endpoint(
            settings={
                'response_type': (SampleCreationBatchItemPagedList,),
                'auth': [
                    'ApiKeyAuth',
                    'JwtAuth'
                ],
                'endpoint_path': '/api/projects/{projectId}/sampleCreationBatch/{batchId}/items',
                'operation_id': 'get_sample_creation_batch_items',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'batch_id',
                    'status',
                    'page_offset',
                    'page_token',
                    'page_size',
                    'sort',
                ],
                'required': [
                    'project_id',
                    'batch_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'status',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('status',): {

                        "INITIALIZED": "INITIALIZED",
                        "WAITING_RESOURCES": "WAITING_RESOURCES",
                        "RUNNING": "RUNNING",
                        "SUCCEEDED": "SUCCEEDED",
                        "PARTIALLY_SUCCEEDED": "PARTIALLY_SUCCEEDED",
                        "FAILED": "FAILED",
                        "STOPPED": "STOPPED"
                    },
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'batch_id':
                        (str,),
                    'status':
                        ([str],),
                    'page_offset':
                        (str,),
                    'page_token':
                        (str,),
                    'page_size':
                        (str,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'batch_id': 'batchId',
                    'status': 'status',
                    'page_offset': 'pageOffset',
                    'page_token': 'pageToken',
                    'page_size': 'pageSize',
                    'sort': 'sort',
                },
                'location_map': {
                    'project_id': 'path',
                    'batch_id': 'path',
                    'status': 'query',
                    'page_offset': 'query',
                    'page_token': 'query',
                    'page_size': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                    'status': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/vnd.illumina.v3+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_sample_creation_batch(
        self,
        project_id,
        create_sample_creation_batch,
        **kwargs
    ):
        """Create a sample creation batch.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_sample_creation_batch(project_id, create_sample_creation_batch, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str):
            create_sample_creation_batch (CreateSampleCreationBatch):

        Keyword Args:
            idempotency_key (str): The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response.</li><li>the request body is not the same as the previous request => 422 error response.</li></ul>This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn't been used in the past 7 days for that specific API and by the specific user.. [optional]
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
            SampleCreationBatch
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
        kwargs['project_id'] = \
            project_id
        kwargs['create_sample_creation_batch'] = \
            create_sample_creation_batch
        return self.create_sample_creation_batch_endpoint.call_with_http_info(**kwargs)

    def get_sample_creation_batch(
        self,
        project_id,
        batch_id,
        **kwargs
    ):
        """Retrieve a sample creation batch.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_sample_creation_batch(project_id, batch_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str):
            batch_id (str): The ID of the sample creation batch

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
            SampleCreationBatch
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
        kwargs['project_id'] = \
            project_id
        kwargs['batch_id'] = \
            batch_id
        return self.get_sample_creation_batch_endpoint.call_with_http_info(**kwargs)

    def get_sample_creation_batch_item(
        self,
        project_id,
        batch_id,
        item_id,
        **kwargs
    ):
        """Retrieve a sample creation batch item.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_sample_creation_batch_item(project_id, batch_id, item_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str):
            batch_id (str): The ID of the sample creation batch
            item_id (str): The ID of the sample creation batch item

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
            SampleCreationBatchSampleItem
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
        kwargs['project_id'] = \
            project_id
        kwargs['batch_id'] = \
            batch_id
        kwargs['item_id'] = \
            item_id
        return self.get_sample_creation_batch_item_endpoint.call_with_http_info(**kwargs)

    def get_sample_creation_batch_items(
        self,
        project_id,
        batch_id,
        **kwargs
    ):
        """Retrieve a list of sample creation batch items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_sample_creation_batch_items(project_id, batch_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str):
            batch_id (str): The ID of the sample creation batch

        Keyword Args:
            status ([str]): The statuses to filter on.. [optional]
            page_offset (str): The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages. [optional]
            page_token (str): The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages.. [optional]
            page_size (str): The amount of rows to return. Use in combination with the offset or cursor parameter to get subsequent results.. [optional]
            sort (str): Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\". [optional]
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
            SampleCreationBatchItemPagedList
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
        kwargs['project_id'] = \
            project_id
        kwargs['batch_id'] = \
            batch_id
        return self.get_sample_creation_batch_items_endpoint.call_with_http_info(**kwargs)

