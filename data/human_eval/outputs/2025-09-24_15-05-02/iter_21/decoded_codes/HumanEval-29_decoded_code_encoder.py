from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix: str) -> List[str]:
    result: List[str] = []
    for string in list_of_strings:
        if string.startswith(prefix):
            result.append(string)
    return result