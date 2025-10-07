from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result: List[str] = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result