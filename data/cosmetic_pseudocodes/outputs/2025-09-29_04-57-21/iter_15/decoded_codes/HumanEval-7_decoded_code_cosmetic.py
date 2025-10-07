from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_results: List[str] = []
    position_tracker: int = 0

    while position_tracker < len(list_of_strings):
        current_element: str = list_of_strings[position_tracker]
        if substring_value in current_element:
            filtered_results.append(current_element)
        position_tracker += 1

    return filtered_results