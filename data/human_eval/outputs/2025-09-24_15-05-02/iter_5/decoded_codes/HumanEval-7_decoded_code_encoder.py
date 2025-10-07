from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for string_element in strings:
        if substring in string_element:
            result.append(string_element)
    return result