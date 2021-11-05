# -*- coding: utf-8 -*-
"""wes module

ImplNote:
Consider implementation here should be reusable application specific routines for WES common use cases.
Consider not to re-do libwes SDK generality.
"""
import logging

from libumccr import libjson

from libica.app import configuration
from libica.openapi import libwes

logger = logging.getLogger(__name__)


def get_run(wfr_id, to_dict=False, to_json=False):
    """
    Get workflow run from WES endpoint ala `ica workflows runs get wfr.81cf25dxxx`

    :param wfr_id:
    :param to_json: False by default
    :param to_dict: False by default
    :return: instance of libwes.WorkflowRun unless to_dict or to_json
    """

    with libwes.ApiClient(configuration(libwes)) as api_client:
        run_api = libwes.WorkflowRunsApi(api_client)
        try:
            logger.info(f"Getting '{wfr_id}' from WES RUN API endpoint")
            wfl_run: libwes.WorkflowRun = run_api.get_workflow_run(run_id=wfr_id)

            if to_dict:
                return wfl_run.to_dict()

            elif to_json:
                return libjson.dumps(wfl_run.to_dict())

            return wfl_run
        except libwes.ApiException as e:
            logger.error(f"Exception when calling get_workflow_run: \n{e}")
