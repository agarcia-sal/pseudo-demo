from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string_value for string_value in strings if string_value.startswith(prefix)]