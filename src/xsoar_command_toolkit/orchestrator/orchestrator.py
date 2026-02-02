import sys
from typing import Dict, Any

from xsoar_command_toolkit.configs import settings
from xsoar_command_toolkit.prompting.prompt_engine import prompt_engine
from xsoar_command_toolkit.orchestrator.cortex_xsoar import CortexXSOAR
from xsoar_command_toolkit.orchestrator.normalize import normalize_json
from xsoar_command_toolkit.orchestrator.payload_builder import payload_builder
from xsoar_command_toolkit.utils.utils import read_a_json


def call_payload_engine(cmd: str, context: Dict = {}) -> bool | Dict:
    payload = False

    if cmd in settings.BYPASS_COMMAND:
        return True
    
    elif cmd == settings.REVOKE_API_COMMAND:
        payload = prompt_engine(questions=settings.REVOKE_API_QUESTIONS, context=context)

    elif cmd == settings.CREATE_INCIDENT_COMMAND:
        payload = prompt_engine(questions=settings.CREATE_INCIDENT_QUESTIONS, context=context)
            
    elif cmd == settings.GET_INCIDENT_COMMAND:
        payload = prompt_engine(questions=settings.GET_INCIDENT_QUESTIONS, context=context)

    elif cmd == settings.SAVE_LIST_COMMAND:
        payload = prompt_engine(questions=settings.SAVE_LIST_QUESTIONS, context=context)
        
    elif cmd == settings.SEARCH_INCIDENTS_COMMAND:
        payload = prompt_engine(questions=settings.SEARCH_INCIDENTS_QUESTIONS, context=context)

    elif cmd == settings.SEARCH_SCRIPT_COMMAND:
        payload = prompt_engine(questions=settings.SEARCH_SCRIPT_QUESTIONS, context=context)
        return payload_builder(cmd=cmd, payload=payload)
    
    elif cmd == settings.UPLOAD_FILE_COMMAND:
        payload = prompt_engine(questions=settings.UPLOAD_FILE_QUESTIONS, context=context)
    
    if payload:
        return payload_builder(cmd=cmd, payload=payload)

    return payload


def call_api_without_payload(cmd: str) -> None | Any:
    api_call = CortexXSOAR()
    results = None

    if cmd == settings.CHECK_HEALTH_COMMAND:
        results = api_call.check_health()

    elif cmd == settings.CHECK_HEALTH_CONTAINERS_COMMAND:
        results = api_call.check_health_containers()

    elif cmd == settings.LOGOUT_MYSELF_COMMAND:
        results = api_call.logout_myself()

    elif cmd == settings.LOGOUT_EVERYONE_COMMAND:
        results = api_call.logout_everyone()

    return results


def call_api_with_payload(cmd: str, body: Dict) -> None | Any:
    api_call = CortexXSOAR()
    results = None

    if cmd == settings.REVOKE_API_COMMAND:
        results = api_call.revoke_api(payload=body)

    elif cmd == settings.CREATE_INCIDENT_COMMAND:
        results = api_call.create_incident(payload=body)

    elif cmd == settings.GET_INCIDENT_COMMAND:
        results = api_call.get_incident(payload=body)

    elif cmd == settings.SAVE_LIST_COMMAND:
        results = api_call.save_list(payload=body)
    
    elif cmd == settings.SEARCH_INCIDENTS_COMMAND:
        results = api_call.search_incidents(payload=body)
    
    elif cmd == settings.SEARCH_SCRIPT_COMMAND:
        results = api_call.search_script(payload=body)
    
    elif cmd == settings.UPLOAD_FILE_COMMAND:
        results = api_call.upload_file(payload=body)

    return results


def orchestrator(input: Dict):
    try:
        results = None
        json_file = {}
        output_args = input

        command = output_args.get('command')
        file_path = output_args.get('path')
            
        if file_path:
            json_file = read_a_json(file_path)
            
        payload = call_payload_engine(cmd=command, context=json_file)

        if isinstance(payload, Dict) and payload:
            results = call_api_with_payload(cmd=command, body=payload)

        elif isinstance(payload, bool) and payload:
            results = call_api_without_payload(cmd=command)
        
        if results:
            normalize_json(results)
                
    except:
        print(settings.USAGE_MESSAGE)
        sys.exit(1)