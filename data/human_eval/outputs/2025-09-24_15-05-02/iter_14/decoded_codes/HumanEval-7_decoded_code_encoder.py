from typing import List

def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    result = []
    for string in list_of_strings:
        if substring in string:
            result.append(string)
    return result