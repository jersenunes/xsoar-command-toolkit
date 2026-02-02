from typing import Dict


def payload_builder(cmd: str, payload: Dict):
    body = {}
    
    for key, value in payload.items():
        if key == 'UsernameRevokeAPI':
            body.update({'user': value})
        
        if key == 'IncidentID':
            body.update({'id': value})

        if key == 'ListName':
            body.update({'name': value})
        
        if key == 'ListContent':
            body.update({'data': value})
        
        if key == 'ListType':
            body.update({'type': value})
        
        if key == 'IncidentName':
            body.update({'name': value})
        
        if key == 'IncidentSeverity':
            body.update({'severity': value})
        
        if key == 'IncidentType':
            body.update({'type': value})
        
        if key == 'IncidentDetails':
            body.update({'details': value})
        
        if key == 'IncidentPlaybook':
            body.update({'playbookId': value})
        
        if key == 'IncidentTime':
            body.update({'created': value})

        if key == 'IncidentStart':
            if value.lower() in ['yes', 'y', 'sim', 's', 'true']:
                body.update({'createInvestigation': True})

            else:
                body.update({'createInvestigation': False})

        if key == 'ScriptName':
            body.update({'name': value})
        
        if key == 'ScriptType':
            body.update({'type': value})

        if key == 'ScriptSystem':
            body.update({'system': value})
        
        if key == 'FilePath':
            body.update({'File': value})
        
        if key == 'IncidentStatus':
            if isinstance(value, int):
                body.update({'status': [value]})

            elif isinstance(value, str) and value.lower == 'pending':
                body.update({'status': [0]})
            
            elif isinstance(value, str) and value.lower == 'active':
                body.update({'status': [1]})
            
            elif isinstance(value, str) and value.lower == 'closed':
                body.update({'status': [2]})

        if cmd == 'Search Incidents':
            body.update({'name': [body.get('name')]})
            body.update({'type': [body.get('type')]})
            body.update({'level': [body.get('severity')]})
            body.update({'andOp': True})
            body.update({'size': 10})
            body.update({'filters': body})

        if cmd == 'Search Script':
            query_string = ''

            if body.get('name'):
                query_string += f'name:{body.get('name')}'

            if body.get('system'):
                query_string += f' and system:{body.get('system')}'

            if body.get('type'):
                query_string += f' and type:{body.get('type')}'

            if query_string:
                body.update({'query': query_string })
    
    return body
