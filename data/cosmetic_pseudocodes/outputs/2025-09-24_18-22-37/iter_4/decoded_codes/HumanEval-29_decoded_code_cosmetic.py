from typing import List

def filter_by_prefix(input_array: List[str], prefix: str) -> List[str]:
    filtered_collection: List[str] = []
    index: int = 0
    while index < len(input_array):
        current_element = input_array[index]
        if current_element.startswith(prefix):
            filtered_collection.append(current_element)
        index += 1
    return filtered_collection