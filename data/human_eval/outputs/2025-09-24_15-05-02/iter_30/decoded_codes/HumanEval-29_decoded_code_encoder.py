from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix: str) -> List[str]:
    return [string_element for string_element in list_of_strings if string_element.startswith(prefix)]