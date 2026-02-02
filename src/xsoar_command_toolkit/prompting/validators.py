from typing import Any

from xsoar_command_toolkit.prompting.errors import ValidationError

def not_empty(value: Any) -> None:
    if value is None:
        raise ValidationError("Value is required.")
    
    if isinstance(value, str) and value.strip() == "":
        raise ValidationError("Value cannot be empty.")
    