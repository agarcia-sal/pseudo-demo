from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    augmented_collection: List[int] = []
    index_counter: int = 0

    while index_counter < len(list_of_elements):
        augmented_collection.append(list_of_elements[index_counter] + 1)
        index_counter += 1

    return augmented_collection