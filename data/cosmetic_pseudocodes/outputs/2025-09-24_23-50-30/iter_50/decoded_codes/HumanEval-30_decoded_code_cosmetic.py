from typing import Sequence, List

def get_positive(sequence_of_values: Sequence[float]) -> List[float]:
    result_collection: List[float] = []
    index_counter: int = 0
    while index_counter < len(sequence_of_values):
        if not (sequence_of_values[index_counter] <= 0):
            result_collection.append(sequence_of_values[index_counter])
        index_counter += 1
    return result_collection