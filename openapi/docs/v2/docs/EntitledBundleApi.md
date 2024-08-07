# libica.openapi.v2.EntitledBundleApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_terms_of_use_entitled_bundle**](EntitledBundleApi.md#accept_terms_of_use_entitled_bundle) | **POST** /api/entitledbundles/{entitledBundleId}/termsOfUse:accept | Accept terms of use for an entitled bundle
[**get_entitled_bundle**](EntitledBundleApi.md#get_entitled_bundle) | **GET** /api/entitledbundles/{entitledBundleId} | Retrieve an entitled bundle.
[**get_entitled_bundle_terms_of_use**](EntitledBundleApi.md#get_entitled_bundle_terms_of_use) | **GET** /api/entitledbundles/{entitledBundleId}/termsOfUse | Retrieve the last version of terms of use for an entitled bundle.
[**get_entitled_bundle_terms_of_use_acceptance**](EntitledBundleApi.md#get_entitled_bundle_terms_of_use_acceptance) | **GET** /api/entitledbundles/{entitledBundleId}/termsOfUse/userAcceptance/currentUser | Retrieve the acceptance record for an entitled bundle for the current user.
[**get_entitled_bundles**](EntitledBundleApi.md#get_entitled_bundles) | **GET** /api/entitledbundles | Retrieve a list of entitled bundles.


# **accept_terms_of_use_entitled_bundle**
> accept_terms_of_use_entitled_bundle(entitled_bundle_id)

Accept terms of use for an entitled bundle

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitled_bundle_api
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entitled_bundle_api.EntitledBundleApi(api_client)
    entitled_bundle_id = "entitledBundleId_example" # str | The ID of the entitled bundle where the terms of use are accepted of.

    # example passing only required values which don't have defaults set
    try:
        # Accept terms of use for an entitled bundle
        api_instance.accept_terms_of_use_entitled_bundle(entitled_bundle_id)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitledBundleApi->accept_terms_of_use_entitled_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitled_bundle_id** | **str**| The ID of the entitled bundle where the terms of use are accepted of. |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The terms of use of the entitled bundle is accepted |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitled_bundle**
> Bundle get_entitled_bundle(entitled_bundle_id)

Retrieve an entitled bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitled_bundle_api
from libica.openapi.v2.model.bundle import Bundle
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entitled_bundle_api.EntitledBundleApi(api_client)
    entitled_bundle_id = "entitledBundleId_example" # str | The ID of the entitled bundle to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an entitled bundle.
        api_response = api_instance.get_entitled_bundle(entitled_bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitledBundleApi->get_entitled_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitled_bundle_id** | **str**| The ID of the entitled bundle to retrieve |

### Return type

[**Bundle**](Bundle.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The entitled bundle is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitled_bundle_terms_of_use**
> TermsOfUse get_entitled_bundle_terms_of_use(entitled_bundle_id)

Retrieve the last version of terms of use for an entitled bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitled_bundle_api
from libica.openapi.v2.model.terms_of_use import TermsOfUse
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entitled_bundle_api.EntitledBundleApi(api_client)
    entitled_bundle_id = "entitledBundleId_example" # str | The ID of the entitled bundle of the terms of use to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the last version of terms of use for an entitled bundle.
        api_response = api_instance.get_entitled_bundle_terms_of_use(entitled_bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitledBundleApi->get_entitled_bundle_terms_of_use: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitled_bundle_id** | **str**| The ID of the entitled bundle of the terms of use to retrieve |

### Return type

[**TermsOfUse**](TermsOfUse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Terms of use are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitled_bundle_terms_of_use_acceptance**
> TermsOfUseAcceptance get_entitled_bundle_terms_of_use_acceptance(entitled_bundle_id)

Retrieve the acceptance record for an entitled bundle for the current user.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitled_bundle_api
from libica.openapi.v2.model.terms_of_use_acceptance import TermsOfUseAcceptance
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entitled_bundle_api.EntitledBundleApi(api_client)
    entitled_bundle_id = "entitledBundleId_example" # str | The ID of the entitled bundle of the terms of use acceptance records.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the acceptance record for an entitled bundle for the current user.
        api_response = api_instance.get_entitled_bundle_terms_of_use_acceptance(entitled_bundle_id)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitledBundleApi->get_entitled_bundle_terms_of_use_acceptance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitled_bundle_id** | **str**| The ID of the entitled bundle of the terms of use acceptance records. |

### Return type

[**TermsOfUseAcceptance**](TermsOfUseAcceptance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Terms of use acceptance is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitled_bundles**
> BundlePagedList get_entitled_bundles()

Retrieve a list of entitled bundles.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):

```python
import time
import libica.openapi.v2
from libica.openapi.v2.api import entitled_bundle_api
from libica.openapi.v2.model.bundle_paged_list import BundlePagedList
from libica.openapi.v2.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = libica.openapi.v2.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = libica.openapi.v2.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with libica.openapi.v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = entitled_bundle_api.EntitledBundleApi(api_client)
    search = "search_example" # str | Search (optional)
    user_tags = "userTags_example" # str | User tags to filter on (optional)
    technical_tags = "technicalTags_example" # str | Technical tags to filter on (optional)
    page_offset = "pageOffset_example" # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = "pageToken_example" # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = "pageSize_example" # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = "sort_example" # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=sortAttribute1, sortAttribute2 desc\"  The attributes for which sorting is supported: - name - shortDescription (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of entitled bundles.
        api_response = api_instance.get_entitled_bundles(search=search, user_tags=user_tags, technical_tags=technical_tags, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        pprint(api_response)
    except libica.openapi.v2.ApiException as e:
        print("Exception when calling EntitledBundleApi->get_entitled_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search | [optional]
 **user_tags** | **str**| User tags to filter on | [optional]
 **technical_tags** | **str**| Technical tags to filter on | [optional]
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional]
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional]
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional]
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;sortAttribute1, sortAttribute2 desc\&quot;  The attributes for which sorting is supported: - name - shortDescription | [optional]

### Return type

[**BundlePagedList**](BundlePagedList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [JwtAuth](../README.md#JwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of entitled bundles is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

