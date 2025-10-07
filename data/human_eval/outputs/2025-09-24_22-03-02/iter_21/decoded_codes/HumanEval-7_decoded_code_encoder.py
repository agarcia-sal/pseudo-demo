from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for index in range(len(strings)):
        x = strings[index]
        if substring in x:
            result.append(x)
    return result