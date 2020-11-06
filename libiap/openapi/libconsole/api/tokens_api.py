# coding: utf-8

"""
    Developer Console Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from libiap.openapi.libconsole.api_client import ApiClient
from libiap.openapi.libconsole.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TokensApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_token(self, **kwargs):  # noqa: E501
        """Creates a JWT token to call IAP services.  # noqa: E501

        This endpoint creates a JWT token to call IAP services. Authorization can be a Bearer psToken,  Basic Base64 encoded username:password or Basic with apiKey.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_api_key: Api Key can be passed in header to generate a JWT.
        :param str client_id: Optionally pass client Id from calling app to set as authorized party on JWT.
        :param str api_key: OBSOLETE: api key should now be passed as as an X-API-Key header.
        :param str domain: Optionally pass the domain name you are logging into
        :param str data: Data is a custom meta data field that will be applied to the session field in the JWT payload.
        :param list[str] scopes: Scopes can be passed in during token generation to limit the token to particular scopes.
        :param str cwid: Set the current workgroup on the token. Used for aligning resources to a workgroup.
        :param str cid: Set the current context on the token. Used for aligning resources to a context.
        :param bool return_session_token: By default, this endpoint returns a JWT token. You can specify returnSessionToken=true to get an Illumina psToken instead.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_token_with_http_info(**kwargs)  # noqa: E501

    def create_token_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a JWT token to call IAP services.  # noqa: E501

        This endpoint creates a JWT token to call IAP services. Authorization can be a Bearer psToken,  Basic Base64 encoded username:password or Basic with apiKey.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_api_key: Api Key can be passed in header to generate a JWT.
        :param str client_id: Optionally pass client Id from calling app to set as authorized party on JWT.
        :param str api_key: OBSOLETE: api key should now be passed as as an X-API-Key header.
        :param str domain: Optionally pass the domain name you are logging into
        :param str data: Data is a custom meta data field that will be applied to the session field in the JWT payload.
        :param list[str] scopes: Scopes can be passed in during token generation to limit the token to particular scopes.
        :param str cwid: Set the current workgroup on the token. Used for aligning resources to a workgroup.
        :param str cid: Set the current context on the token. Used for aligning resources to a context.
        :param bool return_session_token: By default, this endpoint returns a JWT token. You can specify returnSessionToken=true to get an Illumina psToken instead.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TokenResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_api_key',
            'client_id',
            'api_key',
            'domain',
            'data',
            'scopes',
            'cwid',
            'cid',
            'return_session_token'
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
                    " to method create_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'client_id' in local_var_params and local_var_params['client_id'] is not None:  # noqa: E501
            query_params.append(('clientId', local_var_params['client_id']))  # noqa: E501
        if 'api_key' in local_var_params and local_var_params['api_key'] is not None:  # noqa: E501
            query_params.append(('api_key', local_var_params['api_key']))  # noqa: E501
        if 'domain' in local_var_params and local_var_params['domain'] is not None:  # noqa: E501
            query_params.append(('domain', local_var_params['domain']))  # noqa: E501
        if 'data' in local_var_params and local_var_params['data'] is not None:  # noqa: E501
            query_params.append(('data', local_var_params['data']))  # noqa: E501
        if 'scopes' in local_var_params and local_var_params['scopes'] is not None:  # noqa: E501
            query_params.append(('scopes', local_var_params['scopes']))  # noqa: E501
            collection_formats['scopes'] = 'csv'  # noqa: E501
        if 'cwid' in local_var_params and local_var_params['cwid'] is not None:  # noqa: E501
            query_params.append(('cwid', local_var_params['cwid']))  # noqa: E501
        if 'cid' in local_var_params and local_var_params['cid'] is not None:  # noqa: E501
            query_params.append(('cid', local_var_params['cid']))  # noqa: E501
        if 'return_session_token' in local_var_params and local_var_params['return_session_token'] is not None:  # noqa: E501
            query_params.append(('returnSessionToken', local_var_params['return_session_token']))  # noqa: E501

        header_params = {}
        if 'x_api_key' in local_var_params:
            header_params['X-API-Key'] = local_var_params['x_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/tokens', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_details(self, **kwargs):  # noqa: E501
        """Get current tokens info require authorization Bearer token  # noqa: E501

        Get token details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_details(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TokenDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_token_details_with_http_info(**kwargs)  # noqa: E501

    def get_token_details_with_http_info(self, **kwargs):  # noqa: E501
        """Get current tokens info require authorization Bearer token  # noqa: E501

        Get token details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_details_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TokenDetailResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method get_token_details" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/tokens/details', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenDetailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refresh_token(self, **kwargs):  # noqa: E501
        """Refresh session psToken.  # noqa: E501

        This endpoint extends the session for the psToken.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AccessTokenRequest body: Access token request accepts a psToken in the access_token field in the body of the request.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.refresh_token_with_http_info(**kwargs)  # noqa: E501

    def refresh_token_with_http_info(self, **kwargs):  # noqa: E501
        """Refresh session psToken.  # noqa: E501

        This endpoint extends the session for the psToken.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AccessTokenRequest body: Access token request accepts a psToken in the access_token field in the body of the request.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TokenResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'body'
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
                    " to method refresh_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/tokens:refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def revoke_token(self, **kwargs):  # noqa: E501
        """Revokes an access token.  # noqa: E501

        This endpoint revokes the access token that is passed in.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AccessTokenRequest body: Access token request accepts either a psToken or a JWT in the access_token field in the body of the request.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.revoke_token_with_http_info(**kwargs)  # noqa: E501

    def revoke_token_with_http_info(self, **kwargs):  # noqa: E501
        """Revokes an access token.  # noqa: E501

        This endpoint revokes the access token that is passed in.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AccessTokenRequest body: Access token request accepts either a psToken or a JWT in the access_token field in the body of the request.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'body'
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
                    " to method revoke_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Basic', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/tokens', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
