from typing import List

def get_positive(list_of_numbers: List[float]) -> List[float]:
    result_collection: List[float] = []
    index_counter: int = 0
    while index_counter < len(list_of_numbers):
        current_value: float = list_of_numbers[index_counter]
        if not (current_value <= 0):
            result_collection.append(current_value)
        index_counter += 1
    return result_collection