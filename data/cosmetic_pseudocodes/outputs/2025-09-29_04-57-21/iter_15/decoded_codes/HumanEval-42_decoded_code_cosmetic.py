from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    incremented_collection: List[int] = []
    current_index: int = 0
    while current_index < len(list_of_elements):
        current_item: int = list_of_elements[current_index]
        increased_value: int = 1 + current_item
        incremented_collection.append(increased_value)
        current_index += 1
    return incremented_collection