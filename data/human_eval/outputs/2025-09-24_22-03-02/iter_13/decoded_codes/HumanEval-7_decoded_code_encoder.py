from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result_list = []
    for x in strings:
        if substring in x:
            result_list.append(x)
    return result_list