from typing import List

def filter_by_substring(array_input: List[str], string_search: str) -> List[str]:
    filtered_output: List[str] = []
    current_element_INDEX = 0

    while current_element_INDEX < len(array_input):
        if string_search in array_input[current_element_INDEX]:
            filtered_output.append(array_input[current_element_INDEX])
        current_element_INDEX += 1

    return filtered_output