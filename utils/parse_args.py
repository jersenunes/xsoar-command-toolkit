from typing import Dict, List
from configs.settings import *


def parse_args(args: List) -> None | Dict:
    structure = {}
    api_command = ''

    if len(args) == 3:
        if 'cmd=' in args[1]:
            api_command = args[1].replace('cmd=', '')
            file_path = args[2].replace('arg=', '')
            structure.update({'path': file_path})   
            

    if len(args) == 2:
        if 'cmd=' in args[1]:
            api_command = args[1].replace('cmd=')

    for key, value in API_COMMANDS.items():
        if api_command.lower() in value:
            structure.update({'command': key})
            return structure
