"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <b>API-key</b><br> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <b>JWT</b><br> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br> </p> <p> <b>Basic Authentication</b><br> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p>   # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""


import unittest

import libica.openapi.v2
from libica.openapi.v2.api.project_data_transfer_api import ProjectDataTransferApi  # noqa: E501


class TestProjectDataTransferApi(unittest.TestCase):
    """ProjectDataTransferApi unit test stubs"""

    def setUp(self):
        self.api = ProjectDataTransferApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_abort_data_transfer(self):
        """Test case for abort_data_transfer

        Abort a data transfer.  # noqa: E501
        """
        pass

    def test_get_data_transfer(self):
        """Test case for get_data_transfer

        Retrieve a data transfer.  # noqa: E501
        """
        pass

    def test_get_data_transfers(self):
        """Test case for get_data_transfers

        Retrieve a list of data transfers.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
