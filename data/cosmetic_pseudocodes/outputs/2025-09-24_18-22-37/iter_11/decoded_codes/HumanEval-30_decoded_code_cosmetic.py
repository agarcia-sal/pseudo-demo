from typing import List

def get_positive(collection_of_values: List[int]) -> List[int]:
    filtered_collection: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(collection_of_values):
        current_element: int = collection_of_values[iterator_index]
        if current_element > 0:
            filtered_collection.append(current_element)
        iterator_index += 1

    return filtered_collection