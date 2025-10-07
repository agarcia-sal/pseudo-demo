from typing import List

def get_positive(array_of_values: List[int]) -> List[int]:
    filtered_collection: List[int] = []
    for temp_element in array_of_values:
        if temp_element > 0:
            filtered_collection.append(temp_element)
    return filtered_collection