from typing import List

def filter_by_prefix(source_array: List[str], start_sequence: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    prefix_length: int = len(start_sequence)
    while index_counter < len(source_array):
        current_element: str = source_array[index_counter]
        if current_element[:prefix_length] == start_sequence:
            filtered_collection.append(current_element)
        index_counter += 1
    return filtered_collection