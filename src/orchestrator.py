# type: ignore
import sys
from configs.settings import *
from prompting.prompt_engine import prompt_engine
from src.cortex_xsoar import CortexXSOAR
from src.normalize import normalize_json
from src.payload_builder import payload_builder
from utils.parse_args import parse_args
from utils.utils import read_a_json
from typing import List, Dict, Any


def call_payload_engine(cmd: str, context: Dict = {}) -> bool | Dict:
    payload = False

    if cmd in BYPASS_COMMAND:
        return True
    
    elif cmd == 'Revoke API':
        payload = prompt_engine(questions=REVOKE_API_QUESTIONS, context=context)

    elif cmd == 'Create Incident':
        payload = prompt_engine(questions=CREATE_INCIDENT_QUESTIONS, context=context)
            
    elif cmd == 'Get Incident':
        payload = prompt_engine(questions=GET_INCIDENT_QUESTIONS, context=context)

    elif cmd == 'Save List':
        payload = prompt_engine(questions=SAVE_LIST_QUESTIONS, context=context)
        
    elif cmd == 'Search Incidents':
        payload = prompt_engine(questions=SEARCH_INCIDENTS_QUESTIONS, context=context)

    elif cmd == 'Search Script':
        payload = prompt_engine(questions=SEARCH_SCRIPT_QUESTIONS, context=context)
        return payload_builder(cmd=cmd, payload=payload)
    
    elif cmd == 'Upload File':
        payload = prompt_engine(questions=UPLOAD_FILE_QUESTIONS, context=context)
    
    if payload:
        print(payload)
        return payload_builder(cmd=cmd, payload=payload)

    return payload


def call_api_without_payload(cmd: str) -> None | Any:
    api_call = CortexXSOAR()
    results = None

    if cmd == 'Check Health':
        results = api_call.check_health()

    elif cmd == 'Check Health Containers':
        results = api_call.check_health_containers()

    elif cmd == 'Logout Myself':
        results = api_call.logout_myself()

    elif cmd == 'Logout Everyone':
        results = api_call.logout_everyone()

    return results


def call_api_with_payload(cmd: str, body: Dict) -> None | Any:
    api_call = CortexXSOAR()
    results = None

    if cmd == 'Revoke API':
        results = api_call.revoke_api(payload=body)

    elif cmd == 'Create Incident':
        results = api_call.create_incident(payload=body)

    elif cmd == 'Get Incident':
        results = api_call.get_incident(payload=body)

    elif cmd == 'Save List':
        results = api_call.save_list(payload=body)
    
    elif cmd == 'Search Incidents':
        results = api_call.search_incidents(payload=body)
    
    elif cmd == 'Search Script':
        results = api_call.search_script(payload=body)
    
    elif cmd == 'Upload File':
        results = api_call.upload_file(payload=body)

    return results


def orchestrator(input: List):
    try:
        results = None
        json_file = {}
        output_args = parse_args(input)

        command = output_args.get('command')
        file_path = output_args.get('path')
            
        if file_path:
            json_file = read_a_json(file_path)
            
        payload = call_payload_engine(cmd=command, context=json_file)
        print(payload)

        if isinstance(payload, Dict) and payload:
            results = call_api_with_payload(cmd=command, body=payload)

        elif isinstance(payload, bool) and payload:
            results = call_api_without_payload(cmd=command)
        
        if results:
            normalize_json(results)
                
    except:
        #print(USAGE_MESSAGE)
        sys.exit(1)