import os
from pathlib import Path
from dotenv import load_dotenv

#Set .env variables
load_dotenv()
XSOAR_API_KEY = os.getenv('XSOAR_API_KEY')
XSOAR_BASE_URL = os.getenv('XSOAR_BASE_URL')

#Set paths
ROOT_FOLDER = Path(__file__).parent.parent
OUTPUT = ROOT_FOLDER / 'output'
EXAMPLES = ROOT_FOLDER / 'examples'
CERTIFICATE = ROOT_FOLDER / 'certs' / 'cert.pem'

#Set context
BYPASS_COMMAND = ['Check Health', 'Check Health Containers', 'Logout Myself', 'Logout Everyone']
USAGE_MESSAGE = "Commands executed without required arguments will be requested via prompt.\n" \
    "Usage Examples:\n" \
    "python main.py cmd=health\n" \
    "python main.py cmd=logoutmyself\n" \
    "python main.py cmd=logout_everyone\n" \
    "python main.py cmd=delete_api arg=file_path\n" \
    "python main.py cmd=create_incident arg=file_path\n" \
    "python main.py cmd=retrieve_incident arg=file_path\n" \
    "python main.py cmd=setlist arg=file_path\n" \
    "python main.py cmd=search_script arg=file_path\n" \
    "python main.py cmd=uploadfile arg=file_path\n"

API_COMMANDS = {
    'Check Health': ['health', 'checkhealth', 'check_health'],
    'Check Health Containers': ['checkhealthcontainers', 'check_health_containers', 'check_containers', 'checkcontainers', 'containers', 'container'],
    'Logout Myself': ['logout_myself', 'logoutmyself', 'logout', 'signout_myself', 'signoutmyself', 'signout'],
    'Logout Everyone': ['logout_everyone', 'logouteveryone', 'logout_all', 'logoutall', 'logout_members', 'logoutmembers', 'logout_team', 'logoutteam', 'signout_everyone', 'signouteveryone', 'signout_all', 'signoutall', 'signout_members', 'signoutmembers', 'signout_team', 'signoutteam'],
    'Revoke API': ['revoke_api', 'revokeapi', 'remove_api', 'removeapi', 'delete_api', 'deleteapi', 'dell_api', 'dellapi'],
    'Create Incident': ['create_incident', 'createincident', 'make_incident', 'makeincident', 'new_incident', 'newincident'],
    'Get Incident': ['get_incident', 'getincident', 'retrieve_incident', 'retrieveincident'],
    'Save List': ['save_list', 'savelist', 'set_list', 'setlist'],
    'Search Incidents': ['search_incidents', 'searchincidents', 'search_incs', 'searchincs'],
    'Search Script': ['search_script', 'searchscript', 'search_automation', 'searchautomation'],
    'Upload File': ['upload_file', 'uploadfile', 'send_file', 'sendfile']
}

#Set Lists of questions
REVOKE_API_QUESTIONS = [
    {"UsernameRevokeAPI": "Enter the username to revoke the API [REQUIRED]: "}
]
GET_INCIDENT_QUESTIONS = [
    {"IncidentID": "Enter the incident id [REQUIRED]: "}
]
SAVE_LIST_QUESTIONS = [
    {"ListName": "Enter the list name [REQUIRED]: "},
    {"ListType": "Enter the list type (json, csv, plain_text) [default: plain_text]: "},
    {"ListContent": "Enter the list content: "}
]
CREATE_INCIDENT_QUESTIONS = [
    {"IncidentName": "Enter the incident name [REQUIRED]: "},
    {"IncidentSeverity": "Enter the incident severity (between 0 to 4) [default: 0]: "},
    {"IncidentType": "Enter the incident type [default: Unclassified]: "},
    {"IncidentDetails": "Enter the incident details: "},
    {"IncidentPlaybook": "Enter the associated playbook id for this incident [default: default]: "},
    {"IncidentTime": "Enter when this incident has really occurred (ISO Format, example: YYYY-MM-DDThh:mm:ssZ): "},
    {"IncidentStart": "To start the investigation process automatically, answer Yes (Y) or No (N): "}
]
SEARCH_INCIDENTS_QUESTIONS = [
    {"IncidentName": "Enter the incident name: "},
    {"IncidentSeverity": "Enter the incident severity (between 0 to 4): "},
    {"IncidentType": "Enter the incident type: "},
    {"IncidentStatus": "Enter the incident status (0 or Pending, 1 or Active, 2 or Closed): "},
    {"IncidentPlaybook": "Enter the associated playbook id for this incident: "}
]
SEARCH_SCRIPT_QUESTIONS = [
    {"ScriptName": "Enter the script name: "},
    {"ScriptType": "Enter the script type (Python, JavaScript, Powershell): "},
    {"ScriptSystem": "Enter if the script is System (T) ou Custom (F): "}
]
UPLOAD_FILE_QUESTIONS = [
    {"IncidentID": "Enter the incident id [REQUIRED]: "},
    {"FilePath": "Enter the path to the file you want to send for the incident: "}
]