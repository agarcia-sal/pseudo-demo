from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result: List[str] = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        if substring in current_string:
            result.append(current_string)
        index += 1
    return result