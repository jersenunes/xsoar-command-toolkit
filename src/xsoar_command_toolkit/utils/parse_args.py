import sys
from typing import Dict, List

from xsoar_command_toolkit.configs.settings import API_COMMANDS, API_COMMANDS_LIST, HELP_ARGS, USAGE_MESSAGE


def parse_args(args: List) -> None | Dict:
    structure = {}
    api_command = ''

    if len(args) == 3:
        if 'cmd=' in args[1]:
            api_command = args[1].replace('cmd=', '')        
            if 'arg=' in args[2]:
                file_path = args[2].replace('arg=', '')
                structure.update({'path': file_path})

        elif 'cmd=' in args[2]:
            api_command = args[2].replace('cmd=', '')            
            if 'arg=' in args[1]:
                file_path = args[1].replace('arg=', '')
                structure.update({'path': file_path})

        else:
            if args[1] in API_COMMANDS_LIST:
                api_command = args[1]
                if 'arg=' in args[2]:
                    file_path = args[2].replace('arg=', '')
                    structure.update({'path': file_path})

                else:
                    file_path = args[2]
                    structure.update({'path': file_path})

            elif args[2] in API_COMMANDS_LIST:
                api_command = args[2]   
                if 'arg=' in args[1]:
                    file_path = args[1].replace('arg=', '')
                    structure.update({'path': file_path})

                else:
                    file_path = args[1]
                    structure.update({'path': file_path})

        if (args[1].lower() in HELP_ARGS) or (args[2].lower() in HELP_ARGS):
            print(USAGE_MESSAGE)
            sys.exit(1)

    if len(args) == 2:
        if 'cmd=' in args[1]:
            api_command = args[1].replace('cmd=')

        else:
            if args[1] in API_COMMANDS_LIST:
                api_command = args[1]

        if (args[1].lower() in HELP_ARGS):
            print(USAGE_MESSAGE)
            sys.exit(1)

    for key, value in API_COMMANDS.items():
        if api_command.lower() in value:
            structure.update({'command': key})            
            return structure
