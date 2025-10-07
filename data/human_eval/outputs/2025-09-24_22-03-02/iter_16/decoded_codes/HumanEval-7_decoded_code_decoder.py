from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result: List[str] = []
    for x in strings:
        if substring in x:
            result.append(x)
    return result