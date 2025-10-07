from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        candidate = list_of_strings[idx]
        if candidate[:len(prefix_string)] == prefix_string:
            filtered_collection.append(candidate)
        idx += 1
    return filtered_collection