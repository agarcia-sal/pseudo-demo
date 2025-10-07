from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_collection: List[str] = []
    current_index: int = 0

    while current_index < len(list_of_strings):
        candidate: str = list_of_strings[current_index]
        if substring_value not in candidate:
            current_index += 1
            continue

        filtered_collection.append(candidate)
        current_index += 1

    return filtered_collection