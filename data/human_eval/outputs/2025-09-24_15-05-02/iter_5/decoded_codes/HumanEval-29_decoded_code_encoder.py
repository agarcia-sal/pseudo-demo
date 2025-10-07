from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    filtered_strings = []
    for string_element in strings:
        if string_element.startswith(prefix):
            filtered_strings.append(string_element)
    return filtered_strings