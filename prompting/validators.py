from prompting.errors import ValidationError
from typing import Any

def not_empty(value: Any) -> None:
    if value is None:
        raise ValidationError("Value is required.")
    
    if isinstance(value, str) and value.strip() == "":
        raise ValidationError("Value cannot be empty.")
    