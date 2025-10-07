from typing import List


def filter_by_substring(input_strings: List[str], target_substring: str) -> List[str]:
    filtered_list: List[str] = []
    index_counter: int = 0
    while index_counter < len(input_strings):
        current_element: str = input_strings[index_counter]
        if target_substring in current_element:
            filtered_list.append(current_element)
        index_counter += 1
    return filtered_list