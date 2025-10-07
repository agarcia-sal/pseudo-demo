from typing import List

def filter_by_prefix(strings_array: List[str], pref_pattern: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    while idx < len(strings_array):
        current_entry: str = strings_array[idx]
        if current_entry[:len(pref_pattern)] == pref_pattern:
            filtered_collection.append(current_entry)
        idx += 1
    return filtered_collection