from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_strings: List[str] = []
    idx: int = 0
    prefix_length: int = len(prefix_string)
    while idx < len(list_of_strings):
        candidate: str = list_of_strings[idx]
        if candidate[:prefix_length] == prefix_string:
            filtered_strings.append(candidate)
        idx += 1
    return filtered_strings