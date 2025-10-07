from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    new_collection: List[int] = []
    for index in range(len(list_of_elements)):
        current_value = list_of_elements[index]
        incremented_value = current_value + 1
        new_collection.append(incremented_value)
    return new_collection