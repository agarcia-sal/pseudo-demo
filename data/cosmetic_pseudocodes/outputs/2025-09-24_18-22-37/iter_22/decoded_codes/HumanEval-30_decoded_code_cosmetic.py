from typing import Sequence, List

def get_positive(numbers_collection: Sequence[float]) -> List[float]:
    result_collection: List[float] = []
    index_counter: int = 0
    while index_counter < len(numbers_collection):
        current_value = numbers_collection[index_counter]
        if current_value > 0:
            result_collection.append(current_value)
        index_counter += 1
    return result_collection