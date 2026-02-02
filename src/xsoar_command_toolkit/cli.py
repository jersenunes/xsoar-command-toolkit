import sys
from typing import Dict

from xsoar_command_toolkit.configs.settings import USAGE_MESSAGE
from xsoar_command_toolkit.utils.parse_args import parse_args
from xsoar_command_toolkit.main import run_orchestrator


def main() -> None:
    if not sys.argv:
        print(USAGE_MESSAGE)
        sys.exit(1)

    command_arg = parse_args(args=sys.argv)

    if isinstance(command_arg, Dict):
        run_orchestrator(command=command_arg)

if __name__ == '__main__':
    main()
