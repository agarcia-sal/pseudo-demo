from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    filtered_strings = []
    index = 0
    while index < len(strings):
        current_string = strings[index]
        if current_string.startswith(prefix):
            filtered_strings.append(current_string)
        index += 1
    return filtered_strings