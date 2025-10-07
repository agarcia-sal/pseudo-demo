from typing import List

def filter_by_substring(container_strings: List[str], search_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(container_strings):
        current_string: str = container_strings[iterator_index]
        position_indicator: int = current_string.find(search_substring)
        if position_indicator != -1:
            filtered_collection.append(current_string)
        iterator_index += 1
    return filtered_collection