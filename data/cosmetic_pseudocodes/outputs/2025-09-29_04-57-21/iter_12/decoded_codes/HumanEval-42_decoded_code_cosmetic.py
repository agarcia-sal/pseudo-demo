from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result_collection: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(list_of_elements):
        current_value: int = list_of_elements[iterator_index]
        result_collection.append(current_value + 1)
        iterator_index += 1

    return result_collection