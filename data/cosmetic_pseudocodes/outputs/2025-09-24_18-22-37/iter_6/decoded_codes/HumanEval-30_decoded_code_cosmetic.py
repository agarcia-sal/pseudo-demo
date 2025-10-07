from typing import List


def get_positive(array_of_values: List[int]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    while index_counter < len(array_of_values):
        current_entry = array_of_values[index_counter]
        if current_entry > 0:
            result_collection.append(current_entry)
        index_counter += 1
    return result_collection