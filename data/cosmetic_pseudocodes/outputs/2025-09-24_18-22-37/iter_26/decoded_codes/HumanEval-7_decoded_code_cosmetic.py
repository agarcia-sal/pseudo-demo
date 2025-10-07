from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        current_element: str = list_of_strings[idx]
        if substring_value in current_element:
            filtered_collection.append(current_element)
        idx += 1
    return filtered_collection