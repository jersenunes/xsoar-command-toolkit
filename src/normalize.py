# type: ignore
from configs.settings import *
from utils.utils import save_a_json
from datetime import datetime
from typing import Dict


def normalize_json(context: Dict) -> None:
    date_time = datetime.now().replace(microsecond=0).isoformat().replace(":", "-")

    if context.get('Search Script'):
        response = context.get('Search Script')
        for script in response.get('scripts'):
            file_name = script.get('name')
            file_type = script.get('type')
            if file_name and file_type:
                output_file = OUTPUT / f'script-{file_type}-{file_name}-{date_time}.json'
                save_a_json(path=output_file, args=script)
    
    elif context.get('Search Incidents'):
        response = context.get('Search Incidents')
        for incident in response.get('data'):
            incident_name = incident.get('name')
            incident_id = incident.get('id')
            if incident_name and incident_id:
                output_file = OUTPUT / f'incident-{incident_id}-{incident_name}-{date_time}.json'
                save_a_json(path=output_file, args=incident)
    
    else:
        for key, value in context.items():
            output_file = OUTPUT / f'{key}-{date_time}.json'
            save_a_json(path=output_file, args=context)