from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix: str) -> List[str]:
    if not isinstance(prefix, str):
        raise ValueError("prefix must be a string")
    if not all(isinstance(s, str) for s in list_of_strings):
        raise ValueError("list_of_strings must be a list of strings")
    return [string for string in list_of_strings if string.startswith(prefix)]