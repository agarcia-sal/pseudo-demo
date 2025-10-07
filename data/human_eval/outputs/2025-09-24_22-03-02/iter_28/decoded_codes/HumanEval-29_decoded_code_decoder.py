from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result: List[str] = []
    index: int = 0
    while index < len(strings):
        current_string = strings[index]
        if current_string.startswith(prefix) == True:
            result.append(current_string)
        index += 1
    return result