from typing import List

def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    if not isinstance(list_of_strings, list):
        raise ValueError("list_of_strings must be a list")
    if not isinstance(substring, str):
        raise ValueError("substring must be a string")
    return [x for x in list_of_strings if substring in x]