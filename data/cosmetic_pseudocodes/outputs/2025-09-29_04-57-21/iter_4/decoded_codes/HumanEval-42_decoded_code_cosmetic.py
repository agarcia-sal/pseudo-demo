from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    incremented_collection: List[int] = []
    index: int = 0
    while index < len(list_of_elements):
        incremented_collection.append(list_of_elements[index] + 1)
        index += 1
    return incremented_collection