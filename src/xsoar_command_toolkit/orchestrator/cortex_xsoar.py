from pathlib import Path
from typing import Dict

from xsoar_command_toolkit.configs.settings import XSOAR_BASE_URL, XSOAR_API_KEY, CERTIFICATE
from xsoar_command_toolkit.http.client import HTTPClient

class CortexXSOAR:
    def __init__(self) -> None:
        self.__certificate = str(CERTIFICATE)
        self.__endpoint_url = XSOAR_BASE_URL
        self.__headers = {
            "Accept": "application/json",
            "Authorization": XSOAR_API_KEY
        }        


    def check_health(self) -> Dict | str:
        url = self.__endpoint_url + '/health'        
        client = HTTPClient(headers=self.__headers)
        
        response = client.get(url=url, verify=self.__certificate)

        return {'Check Health': response}


    def check_health_containers(self) -> Dict | str:
        url = self.__endpoint_url + '/health/containers'        
        client = HTTPClient(headers=self.__headers)

        response = client.get(url=url, verify=self.__certificate)

        return {'Check Health Containers': response}

    
    def logout_myself(self) -> Dict | str:
        url = self.__endpoint_url + '/logout/myself'        
        client = HTTPClient(headers=self.__headers)

        response = client.post(url=url, verify=self.__certificate)

        return {'Logout Myself': response}

    
    def logout_everyone(self) -> Dict | str:
        url = self.__endpoint_url + '/logout/everyone' 
        client = HTTPClient(headers=self.__headers)

        response = client.post(url=url, verify=self.__certificate)

        return {'Logout Everyone': response}


    def revoke_api(self, payload: Dict) -> Dict | str:
        url = self.__endpoint_url + '/apikeys/revoke/user/' + payload.get('user')
        client = HTTPClient(headers=self.__headers)

        response = client.post(url=url, verify=self.__certificate)

        return {'Revoke API': response}


    def create_incident(self, payload: Dict) -> Dict | str:
        url = self.__endpoint_url + '/incident'
        client = HTTPClient(headers=self.__headers)

        response = client.post(url=url, json=payload, verify=self.__certificate)
    
        return {'Create Incident': response}


    def get_incident(self, payload: Dict) -> Dict | str:
        url = self.__endpoint_url + '/incident/load/' + payload.get('id')
        client = HTTPClient(headers=self.__headers)

        response = client.get(url=url, verify=self.__certificate)
    
        return {'Get Incident': response}
    

    def save_list(self, payload: Dict) -> Dict | str:
        url = self.__endpoint_url + '/lists/save/'
        client = HTTPClient(headers=self.__headers)

        response = client.post(url=url, json=payload, verify=self.__certificate)
        
        return {'Save List': response}
    

    def search_incidents(self, payload: Dict) -> Dict | str:
        url = self.__endpoint_url + '/incidents/search'
        client = HTTPClient(headers=self.__headers)
    
        response = client.post(url=url, json=payload, verify=self.__certificate)

        return {'Search Incidents': response}
    

    def search_script(self, payload: Dict) -> Dict | str:
        url = self.__endpoint_url + '/automation/search/'        
        client = HTTPClient(headers=self.__headers)

        response = client.post(url=url, json=payload, verify=self.__certificate)

        return {'Search Script': response}
    

    def upload_file(self, payload: Dict[str, Path]) -> Dict | str:
        """
        Uploads a file to an incident.

        Returns:
            dict: Parsed JSON response when applicable
            str: Raw response body otherwise
        """
        url = self.__endpoint_url + '/incident/upload/' + payload.get('id')

        data = {
            "fileName": payload.get('file').name,
            "showMediaFile": "true",
            "last": "true"
        }

        with open(payload.get('file'), "rb") as f:
            files = {
                "file": (payload.get('file').name, f, "application/octet-stream")
            }
        
            client = HTTPClient(headers=self.__headers)
            response = client.post(url=url, data=data, files=files, verify=self.__certificate)

        return {'Upload File': response}