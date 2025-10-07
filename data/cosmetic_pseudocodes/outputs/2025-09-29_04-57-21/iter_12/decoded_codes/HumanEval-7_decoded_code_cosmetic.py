from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    result_collection: List[str] = []
    current_index: int = 0

    while current_index < len(list_of_strings):
        element_candidate: str = list_of_strings[current_index]
        if substring_value in element_candidate:
            result_collection.append(element_candidate)
        current_index += 1

    return result_collection