# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from libica.openapi.v2.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from libica.openapi.v2.model.aws_details import AWSDetails
from libica.openapi.v2.model.activation_code_detail import ActivationCodeDetail
from libica.openapi.v2.model.activation_code_detail_list import ActivationCodeDetailList
from libica.openapi.v2.model.activation_code_detail_usage import ActivationCodeDetailUsage
from libica.openapi.v2.model.analysis_base_space_data_details import AnalysisBaseSpaceDataDetails
from libica.openapi.v2.model.analysis_creation_batch import AnalysisCreationBatch
from libica.openapi.v2.model.analysis_creation_batch_item_paged_list_v3 import AnalysisCreationBatchItemPagedListV3
from libica.openapi.v2.model.analysis_creation_batch_item_paged_list_v4 import AnalysisCreationBatchItemPagedListV4
from libica.openapi.v2.model.analysis_creation_batch_item_processing import AnalysisCreationBatchItemProcessing
from libica.openapi.v2.model.analysis_creation_batch_item_request import AnalysisCreationBatchItemRequest
from libica.openapi.v2.model.analysis_creation_batch_item_v3 import AnalysisCreationBatchItemV3
from libica.openapi.v2.model.analysis_creation_batch_item_v4 import AnalysisCreationBatchItemV4
from libica.openapi.v2.model.analysis_data import AnalysisData
from libica.openapi.v2.model.analysis_data_input import AnalysisDataInput
from libica.openapi.v2.model.analysis_external_data import AnalysisExternalData
from libica.openapi.v2.model.analysis_input import AnalysisInput
from libica.openapi.v2.model.analysis_input_data_mount import AnalysisInputDataMount
from libica.openapi.v2.model.analysis_input_external_data import AnalysisInputExternalData
from libica.openapi.v2.model.analysis_input_list import AnalysisInputList
from libica.openapi.v2.model.analysis_output import AnalysisOutput
from libica.openapi.v2.model.analysis_output_list import AnalysisOutputList
from libica.openapi.v2.model.analysis_output_mapping import AnalysisOutputMapping
from libica.openapi.v2.model.analysis_paged_list_v3 import AnalysisPagedListV3
from libica.openapi.v2.model.analysis_paged_list_v4 import AnalysisPagedListV4
from libica.openapi.v2.model.analysis_parameter_input import AnalysisParameterInput
from libica.openapi.v2.model.analysis_query_parameters import AnalysisQueryParameters
from libica.openapi.v2.model.analysis_raw_output import AnalysisRawOutput
from libica.openapi.v2.model.analysis_reference_data_parameter import AnalysisReferenceDataParameter
from libica.openapi.v2.model.analysis_s3_data_details import AnalysisS3DataDetails
from libica.openapi.v2.model.analysis_step import AnalysisStep
from libica.openapi.v2.model.analysis_step_list import AnalysisStepList
from libica.openapi.v2.model.analysis_step_logs import AnalysisStepLogs
from libica.openapi.v2.model.analysis_storage_list_v3 import AnalysisStorageListV3
from libica.openapi.v2.model.analysis_storage_list_v4 import AnalysisStorageListV4
from libica.openapi.v2.model.analysis_storage_v3 import AnalysisStorageV3
from libica.openapi.v2.model.analysis_storage_v4 import AnalysisStorageV4
from libica.openapi.v2.model.analysis_tag import AnalysisTag
from libica.openapi.v2.model.analysis_v3 import AnalysisV3
from libica.openapi.v2.model.analysis_v4 import AnalysisV4
from libica.openapi.v2.model.application import Application
from libica.openapi.v2.model.aws_credentials import AwsCredentials
from libica.openapi.v2.model.aws_temp_credentials import AwsTempCredentials
from libica.openapi.v2.model.base_connection import BaseConnection
from libica.openapi.v2.model.base_job import BaseJob
from libica.openapi.v2.model.base_job_list import BaseJobList
from libica.openapi.v2.model.bundle import Bundle
from libica.openapi.v2.model.bundle_data import BundleData
from libica.openapi.v2.model.bundle_data_linking_batch import BundleDataLinkingBatch
from libica.openapi.v2.model.bundle_data_linking_batch_item import BundleDataLinkingBatchItem
from libica.openapi.v2.model.bundle_data_linking_batch_item_paged_list import BundleDataLinkingBatchItemPagedList
from libica.openapi.v2.model.bundle_data_linking_batch_item_processing import BundleDataLinkingBatchItemProcessing
from libica.openapi.v2.model.bundle_data_linking_batch_item_request import BundleDataLinkingBatchItemRequest
from libica.openapi.v2.model.bundle_data_paged_list import BundleDataPagedList
from libica.openapi.v2.model.bundle_data_unlinking_batch import BundleDataUnlinkingBatch
from libica.openapi.v2.model.bundle_data_unlinking_batch_item import BundleDataUnlinkingBatchItem
from libica.openapi.v2.model.bundle_data_unlinking_batch_item_paged_list import BundleDataUnlinkingBatchItemPagedList
from libica.openapi.v2.model.bundle_data_unlinking_batch_item_processing import BundleDataUnlinkingBatchItemProcessing
from libica.openapi.v2.model.bundle_data_unlinking_batch_item_request import BundleDataUnlinkingBatchItemRequest
from libica.openapi.v2.model.bundle_list import BundleList
from libica.openapi.v2.model.bundle_paged_list import BundlePagedList
from libica.openapi.v2.model.bundle_pipeline import BundlePipeline
from libica.openapi.v2.model.bundle_pipeline_list import BundlePipelineList
from libica.openapi.v2.model.bundle_sample import BundleSample
from libica.openapi.v2.model.bundle_sample_paged_list import BundleSamplePagedList
from libica.openapi.v2.model.bundle_tool import BundleTool
from libica.openapi.v2.model.bundle_tools_list import BundleToolsList
from libica.openapi.v2.model.cwl_tool_definition import CWLToolDefinition
from libica.openapi.v2.model.change_project_owner import ChangeProjectOwner
from libica.openapi.v2.model.complete_folder_upload_session import CompleteFolderUploadSession
from libica.openapi.v2.model.connector import Connector
from libica.openapi.v2.model.connector_list import ConnectorList
from libica.openapi.v2.model.country import Country
from libica.openapi.v2.model.create_analysis_creation_batch import CreateAnalysisCreationBatch
from libica.openapi.v2.model.create_analysis_tag import CreateAnalysisTag
from libica.openapi.v2.model.create_bundle import CreateBundle
from libica.openapi.v2.model.create_bundle_data_linking_batch import CreateBundleDataLinkingBatch
from libica.openapi.v2.model.create_bundle_data_linking_batch_item import CreateBundleDataLinkingBatchItem
from libica.openapi.v2.model.create_bundle_data_unlinking_batch import CreateBundleDataUnlinkingBatch
from libica.openapi.v2.model.create_bundle_data_unlinking_batch_item import CreateBundleDataUnlinkingBatchItem
from libica.openapi.v2.model.create_connector import CreateConnector
from libica.openapi.v2.model.create_custom_event import CreateCustomEvent
from libica.openapi.v2.model.create_custom_notification_subscription import CreateCustomNotificationSubscription
from libica.openapi.v2.model.create_cwl_analysis import CreateCwlAnalysis
from libica.openapi.v2.model.create_data import CreateData
from libica.openapi.v2.model.create_download_rule import CreateDownloadRule
from libica.openapi.v2.model.create_nextflow_analysis import CreateNextflowAnalysis
from libica.openapi.v2.model.create_notification_channel import CreateNotificationChannel
from libica.openapi.v2.model.create_notification_subscription import CreateNotificationSubscription
from libica.openapi.v2.model.create_project import CreateProject
from libica.openapi.v2.model.create_project_data_copy_batch import CreateProjectDataCopyBatch
from libica.openapi.v2.model.create_project_data_copy_batch_item import CreateProjectDataCopyBatchItem
from libica.openapi.v2.model.create_project_data_linking_batch import CreateProjectDataLinkingBatch
from libica.openapi.v2.model.create_project_data_linking_batch_item import CreateProjectDataLinkingBatchItem
from libica.openapi.v2.model.create_project_data_move_batch import CreateProjectDataMoveBatch
from libica.openapi.v2.model.create_project_data_move_batch_item import CreateProjectDataMoveBatchItem
from libica.openapi.v2.model.create_project_data_unlinking_batch import CreateProjectDataUnlinkingBatch
from libica.openapi.v2.model.create_project_data_unlinking_batch_item import CreateProjectDataUnlinkingBatchItem
from libica.openapi.v2.model.create_project_data_update_batch import CreateProjectDataUpdateBatch
from libica.openapi.v2.model.create_project_permission import CreateProjectPermission
from libica.openapi.v2.model.create_project_permission_v4 import CreateProjectPermissionV4
from libica.openapi.v2.model.create_sample import CreateSample
from libica.openapi.v2.model.create_sample_creation_batch import CreateSampleCreationBatch
from libica.openapi.v2.model.create_sample_creation_batch_data_item import CreateSampleCreationBatchDataItem
from libica.openapi.v2.model.create_sample_creation_batch_sample_item import CreateSampleCreationBatchSampleItem
from libica.openapi.v2.model.create_storage_configuration import CreateStorageConfiguration
from libica.openapi.v2.model.create_storage_credential import CreateStorageCredential
from libica.openapi.v2.model.create_temporary_credentials import CreateTemporaryCredentials
from libica.openapi.v2.model.create_terms_of_use import CreateTermsOfUse
from libica.openapi.v2.model.create_upload_rule import CreateUploadRule
from libica.openapi.v2.model.custom_notification_subscription import CustomNotificationSubscription
from libica.openapi.v2.model.custom_notification_subscription_list import CustomNotificationSubscriptionList
from libica.openapi.v2.model.cwl_analysis_input import CwlAnalysisInput
from libica.openapi.v2.model.cwl_analysis_input_json import CwlAnalysisInputJson
from libica.openapi.v2.model.cwl_analysis_json_input import CwlAnalysisJsonInput
from libica.openapi.v2.model.cwl_analysis_output_json import CwlAnalysisOutputJson
from libica.openapi.v2.model.cwl_analysis_structured_input import CwlAnalysisStructuredInput
from libica.openapi.v2.model.cwl_tool_definition_list import CwlToolDefinitionList
from libica.openapi.v2.model.data import Data
from libica.openapi.v2.model.data_details import DataDetails
from libica.openapi.v2.model.data_format import DataFormat
from libica.openapi.v2.model.data_format_paged_list import DataFormatPagedList
from libica.openapi.v2.model.data_id_or_path_list import DataIdOrPathList
from libica.openapi.v2.model.data_list import DataList
from libica.openapi.v2.model.data_paged_list import DataPagedList
from libica.openapi.v2.model.data_tag import DataTag
from libica.openapi.v2.model.data_transfer import DataTransfer
from libica.openapi.v2.model.data_transfer_paged_list import DataTransferPagedList
from libica.openapi.v2.model.data_update_group import DataUpdateGroup
from libica.openapi.v2.model.data_url_with_path import DataUrlWithPath
from libica.openapi.v2.model.data_url_with_path_list import DataUrlWithPathList
from libica.openapi.v2.model.download import Download
from libica.openapi.v2.model.download_rule import DownloadRule
from libica.openapi.v2.model.download_rule_list import DownloadRuleList
from libica.openapi.v2.model.event_code import EventCode
from libica.openapi.v2.model.event_code_list import EventCodeList
from libica.openapi.v2.model.event_log_list_v3 import EventLogListV3
from libica.openapi.v2.model.event_log_paged_list_v4 import EventLogPagedListV4
from libica.openapi.v2.model.event_log_query_parameters_v4 import EventLogQueryParametersV4
from libica.openapi.v2.model.event_log_v3 import EventLogV3
from libica.openapi.v2.model.event_log_v4 import EventLogV4
from libica.openapi.v2.model.execution_configuration import ExecutionConfiguration
from libica.openapi.v2.model.execution_configuration_list import ExecutionConfigurationList
from libica.openapi.v2.model.field import Field
from libica.openapi.v2.model.field_id import FieldId
from libica.openapi.v2.model.field_list import FieldList
from libica.openapi.v2.model.find_project_samples import FindProjectSamples
from libica.openapi.v2.model.find_sample_boolean_condition import FindSampleBooleanCondition
from libica.openapi.v2.model.find_sample_condition import FindSampleCondition
from libica.openapi.v2.model.find_sample_date_condition import FindSampleDateCondition
from libica.openapi.v2.model.find_sample_number_condition import FindSampleNumberCondition
from libica.openapi.v2.model.folder_upload_session import FolderUploadSession
from libica.openapi.v2.model.inline_view import InlineView
from libica.openapi.v2.model.input_parameter import InputParameter
from libica.openapi.v2.model.input_parameter_list import InputParameterList
from libica.openapi.v2.model.input_part import InputPart
from libica.openapi.v2.model.input_part_media_type import InputPartMediaType
from libica.openapi.v2.model.integer_settings import IntegerSettings
from libica.openapi.v2.model.job import Job
from libica.openapi.v2.model.job_paged_list import JobPagedList
from libica.openapi.v2.model.link import Link
from libica.openapi.v2.model.links import Links
from libica.openapi.v2.model.load_data_in_base_request import LoadDataInBaseRequest
from libica.openapi.v2.model.metadata_field import MetadataField
from libica.openapi.v2.model.metadata_model import MetadataModel
from libica.openapi.v2.model.metadata_model_list import MetadataModelList
from libica.openapi.v2.model.model import Model
from libica.openapi.v2.model.multipart_form_data_input import MultipartFormDataInput
from libica.openapi.v2.model.nextflow_analysis_input import NextflowAnalysisInput
from libica.openapi.v2.model.notification_channel import NotificationChannel
from libica.openapi.v2.model.notification_channel_list import NotificationChannelList
from libica.openapi.v2.model.notification_subscription import NotificationSubscription
from libica.openapi.v2.model.notification_subscription_list import NotificationSubscriptionList
from libica.openapi.v2.model.option_settings import OptionSettings
from libica.openapi.v2.model.optional_sample_tags import OptionalSampleTags
from libica.openapi.v2.model.pipeline_bundle import PipelineBundle
from libica.openapi.v2.model.pipeline_configuration_parameter import PipelineConfigurationParameter
from libica.openapi.v2.model.pipeline_configuration_parameter_list import PipelineConfigurationParameterList
from libica.openapi.v2.model.pipeline_file import PipelineFile
from libica.openapi.v2.model.pipeline_file_list import PipelineFileList
from libica.openapi.v2.model.pipeline_html_documentation import PipelineHtmlDocumentation
from libica.openapi.v2.model.pipeline_language_version import PipelineLanguageVersion
from libica.openapi.v2.model.pipeline_language_version_list import PipelineLanguageVersionList
from libica.openapi.v2.model.pipeline_list import PipelineList
from libica.openapi.v2.model.pipeline_tag import PipelineTag
from libica.openapi.v2.model.pipeline_v3 import PipelineV3
from libica.openapi.v2.model.pipeline_v4 import PipelineV4
from libica.openapi.v2.model.problem import Problem
from libica.openapi.v2.model.project import Project
from libica.openapi.v2.model.project_base_table import ProjectBaseTable
from libica.openapi.v2.model.project_base_table_list import ProjectBaseTableList
from libica.openapi.v2.model.project_bundle import ProjectBundle
from libica.openapi.v2.model.project_bundle_list import ProjectBundleList
from libica.openapi.v2.model.project_data import ProjectData
from libica.openapi.v2.model.project_data_copy_batch import ProjectDataCopyBatch
from libica.openapi.v2.model.project_data_copy_batch_item import ProjectDataCopyBatchItem
from libica.openapi.v2.model.project_data_copy_batch_item_paged_list import ProjectDataCopyBatchItemPagedList
from libica.openapi.v2.model.project_data_copy_batch_item_processing import ProjectDataCopyBatchItemProcessing
from libica.openapi.v2.model.project_data_copy_batch_item_request import ProjectDataCopyBatchItemRequest
from libica.openapi.v2.model.project_data_linking_batch import ProjectDataLinkingBatch
from libica.openapi.v2.model.project_data_linking_batch_item import ProjectDataLinkingBatchItem
from libica.openapi.v2.model.project_data_linking_batch_item_paged_list import ProjectDataLinkingBatchItemPagedList
from libica.openapi.v2.model.project_data_linking_batch_item_paged_list_v4 import ProjectDataLinkingBatchItemPagedListV4
from libica.openapi.v2.model.project_data_linking_batch_item_processing import ProjectDataLinkingBatchItemProcessing
from libica.openapi.v2.model.project_data_linking_batch_item_processing_v4 import ProjectDataLinkingBatchItemProcessingV4
from libica.openapi.v2.model.project_data_linking_batch_item_request import ProjectDataLinkingBatchItemRequest
from libica.openapi.v2.model.project_data_linking_batch_item_v4 import ProjectDataLinkingBatchItemV4
from libica.openapi.v2.model.project_data_move_batch import ProjectDataMoveBatch
from libica.openapi.v2.model.project_data_move_batch_item import ProjectDataMoveBatchItem
from libica.openapi.v2.model.project_data_move_batch_item_paged_list import ProjectDataMoveBatchItemPagedList
from libica.openapi.v2.model.project_data_move_batch_item_processing import ProjectDataMoveBatchItemProcessing
from libica.openapi.v2.model.project_data_move_batch_item_query_parameters import ProjectDataMoveBatchItemQueryParameters
from libica.openapi.v2.model.project_data_move_batch_item_request import ProjectDataMoveBatchItemRequest
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList
from libica.openapi.v2.model.project_data_unlinking_batch import ProjectDataUnlinkingBatch
from libica.openapi.v2.model.project_data_unlinking_batch_item import ProjectDataUnlinkingBatchItem
from libica.openapi.v2.model.project_data_unlinking_batch_item_paged_list import ProjectDataUnlinkingBatchItemPagedList
from libica.openapi.v2.model.project_data_unlinking_batch_item_processing import ProjectDataUnlinkingBatchItemProcessing
from libica.openapi.v2.model.project_data_unlinking_batch_item_request import ProjectDataUnlinkingBatchItemRequest
from libica.openapi.v2.model.project_data_update_batch import ProjectDataUpdateBatch
from libica.openapi.v2.model.project_data_update_batch_item import ProjectDataUpdateBatchItem
from libica.openapi.v2.model.project_data_update_batch_item_paged_list import ProjectDataUpdateBatchItemPagedList
from libica.openapi.v2.model.project_data_update_batch_item_processing import ProjectDataUpdateBatchItemProcessing
from libica.openapi.v2.model.project_data_update_batch_item_request import ProjectDataUpdateBatchItemRequest
from libica.openapi.v2.model.project_list import ProjectList
from libica.openapi.v2.model.project_paged_list import ProjectPagedList
from libica.openapi.v2.model.project_permission import ProjectPermission
from libica.openapi.v2.model.project_permission_list import ProjectPermissionList
from libica.openapi.v2.model.project_permission_list_v4 import ProjectPermissionListV4
from libica.openapi.v2.model.project_permission_v4 import ProjectPermissionV4
from libica.openapi.v2.model.project_pipeline import ProjectPipeline
from libica.openapi.v2.model.project_pipeline_list import ProjectPipelineList
from libica.openapi.v2.model.project_sample import ProjectSample
from libica.openapi.v2.model.project_sample_paged_list import ProjectSamplePagedList
from libica.openapi.v2.model.project_tag import ProjectTag
from libica.openapi.v2.model.rclone_temp_credentials import RcloneTempCredentials
from libica.openapi.v2.model.reference_data import ReferenceData
from libica.openapi.v2.model.reference_data_list import ReferenceDataList
from libica.openapi.v2.model.reference_data_type import ReferenceDataType
from libica.openapi.v2.model.reference_data_type_list import ReferenceDataTypeList
from libica.openapi.v2.model.reference_set import ReferenceSet
from libica.openapi.v2.model.reference_set_list import ReferenceSetList
from libica.openapi.v2.model.region import Region
from libica.openapi.v2.model.region_list import RegionList
from libica.openapi.v2.model.sample import Sample
from libica.openapi.v2.model.sample_creation_batch import SampleCreationBatch
from libica.openapi.v2.model.sample_creation_batch_item_paged_list import SampleCreationBatchItemPagedList
from libica.openapi.v2.model.sample_creation_batch_item_processing import SampleCreationBatchItemProcessing
from libica.openapi.v2.model.sample_creation_batch_item_request import SampleCreationBatchItemRequest
from libica.openapi.v2.model.sample_creation_batch_sample_item import SampleCreationBatchSampleItem
from libica.openapi.v2.model.sample_history import SampleHistory
from libica.openapi.v2.model.sample_history_list import SampleHistoryList
from libica.openapi.v2.model.sample_paged_list import SamplePagedList
from libica.openapi.v2.model.sample_tag import SampleTag
from libica.openapi.v2.model.schedule_download import ScheduleDownload
from libica.openapi.v2.model.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
from libica.openapi.v2.model.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
from libica.openapi.v2.model.sequencing_run import SequencingRun
from libica.openapi.v2.model.settings import Settings
from libica.openapi.v2.model.species import Species
from libica.openapi.v2.model.species_list import SpeciesList
from libica.openapi.v2.model.storage_bundle import StorageBundle
from libica.openapi.v2.model.storage_bundle_list import StorageBundleList
from libica.openapi.v2.model.storage_configuration import StorageConfiguration
from libica.openapi.v2.model.storage_configuration_details import StorageConfigurationDetails
from libica.openapi.v2.model.storage_configuration_with_details import StorageConfigurationWithDetails
from libica.openapi.v2.model.storage_configuration_with_details_list import StorageConfigurationWithDetailsList
from libica.openapi.v2.model.storage_credential import StorageCredential
from libica.openapi.v2.model.storage_credential_list import StorageCredentialList
from libica.openapi.v2.model.string_settings import StringSettings
from libica.openapi.v2.model.system_info import SystemInfo
from libica.openapi.v2.model.tag_update import TagUpdate
from libica.openapi.v2.model.temp_credentials import TempCredentials
from libica.openapi.v2.model.tenant_identifier import TenantIdentifier
from libica.openapi.v2.model.terms_of_use import TermsOfUse
from libica.openapi.v2.model.terms_of_use_acceptance import TermsOfUseAcceptance
from libica.openapi.v2.model.token import Token
from libica.openapi.v2.model.update_metadata import UpdateMetadata
from libica.openapi.v2.model.update_metadata_field_group import UpdateMetadataFieldGroup
from libica.openapi.v2.model.update_single_metadata_field import UpdateSingleMetadataField
from libica.openapi.v2.model.update_storage_credential_secrets import UpdateStorageCredentialSecrets
from libica.openapi.v2.model.upload import Upload
from libica.openapi.v2.model.upload_rule import UploadRule
from libica.openapi.v2.model.upload_rule_list import UploadRuleList
from libica.openapi.v2.model.user import User
from libica.openapi.v2.model.user_identifier import UserIdentifier
from libica.openapi.v2.model.user_list import UserList
from libica.openapi.v2.model.workflow_session_analysis_paged_list_v4 import WorkflowSessionAnalysisPagedListV4
from libica.openapi.v2.model.workflow_session_analysis_v4 import WorkflowSessionAnalysisV4
from libica.openapi.v2.model.workflow_session_configuration import WorkflowSessionConfiguration
from libica.openapi.v2.model.workflow_session_configuration_list import WorkflowSessionConfigurationList
from libica.openapi.v2.model.workflow_session_data import WorkflowSessionData
from libica.openapi.v2.model.workflow_session_external_data import WorkflowSessionExternalData
from libica.openapi.v2.model.workflow_session_input import WorkflowSessionInput
from libica.openapi.v2.model.workflow_session_input_list import WorkflowSessionInputList
from libica.openapi.v2.model.workflow_session_paged_list_v3 import WorkflowSessionPagedListV3
from libica.openapi.v2.model.workflow_session_paged_list_v4 import WorkflowSessionPagedListV4
from libica.openapi.v2.model.workflow_session_tag import WorkflowSessionTag
from libica.openapi.v2.model.workflow_session_v3 import WorkflowSessionV3
from libica.openapi.v2.model.workflow_session_v4 import WorkflowSessionV4
from libica.openapi.v2.model.workflow_v3 import WorkflowV3
from libica.openapi.v2.model.workflow_v4 import WorkflowV4
from libica.openapi.v2.model.workgroup import Workgroup
from libica.openapi.v2.model.workgroup_list import WorkgroupList
