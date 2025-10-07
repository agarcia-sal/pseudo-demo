from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_strings: List[str] = []
    index: int = 0
    while index < len(strings):
        current_string: str = strings[index]
        if substring in current_string:
            filtered_strings.append(current_string)
        index += 1
    return filtered_strings