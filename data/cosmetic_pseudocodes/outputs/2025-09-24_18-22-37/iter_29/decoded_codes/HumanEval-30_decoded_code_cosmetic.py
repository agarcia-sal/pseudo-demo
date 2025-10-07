from typing import List


def get_positive(array_of_values: List[int]) -> List[int]:
    filtered_collection: List[int] = []
    cursor: int = 0
    while cursor < len(array_of_values):
        current_element: int = array_of_values[cursor]
        if current_element > 0:
            filtered_collection.append(current_element)
        cursor += 1
    return filtered_collection