from typing import List

def filter_by_prefix(array_values: List[str], matching_prefix: str) -> List[str]:
    result_collection: List[str] = []
    index_counter: int = 0
    prefix_length: int = len(matching_prefix)
    while index_counter < len(array_values):
        current_element: str = array_values[index_counter]
        if current_element[:prefix_length] == matching_prefix:
            result_collection.append(current_element)
        index_counter += 1
    return result_collection