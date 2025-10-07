from typing import List

def filter_by_substring(array_of_strings: List[str], target_substring: str) -> List[str]:
    index_tracker: int = 0
    filtered_collection: List[str] = []
    while index_tracker < len(array_of_strings):
        # Using a switch-like construct with if-else to decide inclusion
        if target_substring not in array_of_strings[index_tracker]:
            index_tracker += 1
            continue
        else:
            filtered_collection.append(array_of_strings[index_tracker])
            index_tracker += 1
    return filtered_collection