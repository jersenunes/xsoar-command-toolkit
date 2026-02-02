from typing import Dict
from xsoar_command_toolkit.orchestrator.orchestrator import orchestrator


def run_orchestrator(command: Dict):

    orchestrator(input=command)

