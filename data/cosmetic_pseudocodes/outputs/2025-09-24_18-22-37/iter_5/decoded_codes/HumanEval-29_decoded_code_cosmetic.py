from typing import List

def filter_by_prefix(input_array: List[str], start_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    index: int = 0
    total_elements: int = len(input_array)
    while index < total_elements:
        current_element: str = input_array[index]
        prefix_length: int = len(start_substring)
        element_prefix: str = current_element[:prefix_length]
        if element_prefix == start_substring:
            filtered_collection.append(current_element)
        index += 1
    return filtered_collection