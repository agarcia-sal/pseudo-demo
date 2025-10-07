from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result = []
    i = 0
    while i < len(strings):
        current_string = strings[i]
        starts_with_prefix = current_string.startswith(prefix)
        if starts_with_prefix:
            result.append(current_string)
        i += 1
    return result