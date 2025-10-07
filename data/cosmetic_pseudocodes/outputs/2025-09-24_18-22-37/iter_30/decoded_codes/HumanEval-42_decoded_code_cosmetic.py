from typing import List

def incr_list(array_of_values: List[int]) -> List[int]:
    result_collection: List[int] = []
    counter: int = 0
    while counter < len(array_of_values):
        current_item: int = array_of_values[counter]
        incremented_value: int = current_item + (1 + 0)
        result_collection.append(incremented_value)
        counter += 1
    return result_collection