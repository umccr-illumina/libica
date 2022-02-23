# libica

[![Pull Request Build Status](https://github.com/umccr-illumina/libica/workflows/Pull%20Request%20Build/badge.svg)](https://github.com/umccr-illumina/libica/actions) [![PyPI - Downloads](https://img.shields.io/pypi/dm/libica?style=flat)](https://pypistats.org/packages/libica) [![PyPI](https://img.shields.io/pypi/v/libica?style=flat)](https://pypi.org/project/libica) 
[![PyPI - License](https://img.shields.io/pypi/l/libica?style=flat)](https://opensource.org/licenses/MIT)

Python SDK to programmatically call Illumina Connected Analytics (ICA). Supported the following APIs:

- API v1: https://ica-docs.readme.io/reference
- API v2: https://illumina.gitbook.io/ica/reference/r-api
- Install through ``pip`` like so:
```commandline
pip install libica
```

**Overview:**

- Tested for Python 3.6, 3.7, 3.8, 3.9
- https://umccr-illumina.github.io/libica/
- [Test Coverage](https://umccr-illumina.github.io/libica/coverage/)
- [PyDoc](https://umccr-illumina.github.io/libica/libica/)
- [Wiki](https://github.com/umccr-illumina/libica/wiki)

## Getting started with SDK for ICA v2

See [pilot.py](pilot.py)

```python
# List all data in a project
import os
from contextlib import closing

from libica.openapi.v2 import Configuration, ApiClient, ApiException
from libica.openapi.v2.api.project_data_api import ProjectDataApi
from libica.openapi.v2.model.project_data import ProjectData
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList

if __name__ == '__main__':

    project_id = os.environ['ICA_PROJECT']
    file_path = [""]  # empty will list everything under project

    icav2_access_token = os.environ['ICAV2_ACCESS_TOKEN']
    ica_url = "https://ica.illumina.com/ica/rest"

    configuration = Configuration(
        host=ica_url,
        access_token=icav2_access_token,
    )
    # configuration.debug = True  # uncomment to debug API call logging

    api_client = ApiClient(
        configuration=configuration,
        header_name="Content-Type",
        header_value="application/vnd.illumina.v3+json",
    )

    with closing(api_client) as ctx_api_client:
        project_data_api: ProjectDataApi = ProjectDataApi(api_client=ctx_api_client)

        try:
            page_token = ""
            while True:
                project_data_paged_list: ProjectDataPagedList = project_data_api.get_project_data_list(
                    project_id=project_id,
                    file_path=file_path,
                    page_size=str(1000),
                    page_token=page_token,
                )

                for item in project_data_paged_list.items:
                    project_data: ProjectData = item
                    print((
                        project_data.data.id,  # fil.<ID> (or) fol.<ID>
                        project_data.data.details.path,
                        project_data.data.details.data_type,
                    ))

                page_token = project_data_paged_list.next_page_token
                if not project_data_paged_list.next_page_token:
                    break

        except ApiException as e:
            print(e)
```

## Getting started with SDK for ICA v1

- Export ICA base URL and JWT Bearer token:
```
export ICA_BASE_URL=<baseUrl>
export ICA_ACCESS_TOKEN=<tok>
```

- Generate Bearer JWT token using [ICA CLI](https://sapac.support.illumina.com/sequencing/sequencing_software/illumina-connected-analytics.html) like so:
```commandline
ica tokens create --help
```

- Somewhere in your Python code:
```python
import os
from libica.openapi import libwes
from libica.openapi.libwes import WorkflowList, WorkflowCompact

ica_base_url = os.getenv("ICA_BASE_URL")
ica_access_token = os.getenv("ICA_ACCESS_TOKEN")

configuration = libwes.Configuration(
    host=ica_base_url,
    api_key={
        'Authorization': ica_access_token
    },
    api_key_prefix={
        'Authorization': "Bearer"
    },
)

with libwes.ApiClient(configuration) as api_client:

    wfl_api: libwes.WorkflowsApi = libwes.WorkflowsApi(api_client)
    try:
        page_token = None
        while True:
            wfl_list: WorkflowList = wfl_api.list_workflows(page_size=100, page_token=page_token)
            # print(wfl_list)
            for item in wfl_list.items:
                wfl: WorkflowCompact = item
                print(wfl.id)
                print(wfl.name)
            page_token = wfl_list.next_page_token
            if not wfl_list.next_page_token:
                break
    except libwes.ApiException as e:
        print(e)
```

## Using App Package

> NOTE: `libica.app` package contains reusable modules that are based on use cases around UMCCR Data Portal backend, CWL Workflows and its orchestration implementations. Hence, it may be a specific implementation, however, it can still be reusable for your cases. Please have a look [into package](libica/app) and quick starter examples are as follows.

### App for ICA v2

See [pilotapp.py](pilotapp.py)

Example: `DataOps` app to list project files, download a file, etc...

```python
from contextlib import closing

from libica.app import AppHelper
from libica.app.dataops import ProjectDataOps
from libica.openapi.v2 import ApiClient
from libica.openapi.v2.model.project_data import ProjectData

app_helper = AppHelper(debug=False)
project_id = app_helper.get_icav2_cli_session_project_id()

cli_session_api_client: ApiClient = app_helper \
    .build_icav2_configuration_with_cli_session() \
    .get_icav2_api_client()

dataops = ProjectDataOps(project_id=project_id, api_client=cli_session_api_client)

for item in dataops.list_files():
    project_data: ProjectData = item
    print((
        project_data.data.id,  # fil.<ID> (or) fol.<ID>
        project_data.data.details.path,
        project_data.data.details.data_type,
        project_data.data.details.name,
        project_data.data.details.status,
        project_data.data.details.file_size_in_bytes,
        project_data.data.details.time_created,
    ))

file_path = "/test_folder/SampleSheet.csv"
print(f"Downloading {file_path} from project_id {project_id}")
ntf = dataops.download_file(file_path=file_path)
with closing(ntf) as cf:
    with open(cf.name, 'r') as f:
        for line in f.readlines():
            print(line)
```

### App for ICA v1

Example: Configuration Object Builder

```python
from libica.app import configuration
from libica.openapi import libgds

gds_config = configuration(
  lib=libgds,  # pass in library of interest e.g. libwes, libtes, etc 
  secret_name=["FROM_AWS_SECRET_MANAGER_THAT_STORE_ICA_ACCESS_TOKEN"],
  base_url="https://use1.platform.illumina.com",  # overwrite if not https://aps2.platform.illumina.com
  debug=False,  # True if you like to debug API calls, False by default anyway, just for demo
)

with libgds.ApiClient(gds_config) as api_client:
    ...
```

Example: Listing Files from GDS

```python
from typing import List

from libica.app import gds
from libica.openapi import libgds

vol, path = gds.parse_path("gds://development/some/folder/path/")
files: List[libgds.FileResponse] = gds.get_file_list(volume_name=vol, path=path)

for file in files:
  print(f"{file.name}, {file.volume_name}, {file.path}, {file.presigned_url}")
```

## Development

- Setup virtual environment and activate it

- Install dev dependencies
```commandline
make install
```

- To bring up _mock_ API _μ_-services
```commandline
make up
```

- To run tests suites
```commandline
make unit
make autounit
```

- To run full suite, smoke test
```commandline
make test
```

### AutoGen Workflow

- SDK is autogenerated from respective endpoint OpenAPI (Swagger) definitions
- There are few key CLI tools for this autogen workflow to work.
    1. [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) -- used to generate code and doc
    2. [swagger-cli](https://github.com/APIDevTools/swagger-cli) -- validate definitions
- These CLI tools are Node.js app, hence, required build tools `node`, `npm`, `npx` and `yarn` as follows.
```commandline
node -v
 v14.19.0
npm -i -g yarn
yarn install
npx openapi-generator-cli help
npx swagger-cli --help
```
- However, `prism` mock server is set up through docker compose as follows.
```
make up
make test_ica_mock
docker-compose logs
docker-compose ps
docker ps
```
- All the autogen config and arrangement refer to [`syncapi.sh`](syncapi.sh) and [`syncapi2.sh`](syncapi2.sh) which is called through [`Makefile`](Makefile) targets.

#### Generator Version

- See generator [version compatibility](https://github.com/OpenAPITools/openapi-generator#11---compatibility)
- Select generator version as follows:

```
npx openapi-generator-cli version-manager list
```

## License

MIT License and DISCLAIMER

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
