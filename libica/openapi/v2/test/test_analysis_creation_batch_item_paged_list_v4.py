"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p>   # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import libica.openapi.v2
from libica.openapi.v2.model.analysis_creation_batch_item_v4 import AnalysisCreationBatchItemV4
globals()['AnalysisCreationBatchItemV4'] = AnalysisCreationBatchItemV4
from libica.openapi.v2.model.analysis_creation_batch_item_paged_list_v4 import AnalysisCreationBatchItemPagedListV4


class TestAnalysisCreationBatchItemPagedListV4(unittest.TestCase):
    """AnalysisCreationBatchItemPagedListV4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnalysisCreationBatchItemPagedListV4(self):
        """Test AnalysisCreationBatchItemPagedListV4"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AnalysisCreationBatchItemPagedListV4()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
