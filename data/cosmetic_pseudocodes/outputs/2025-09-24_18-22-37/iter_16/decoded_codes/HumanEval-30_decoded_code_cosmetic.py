from typing import Sequence, List

def get_positive(sequence_of_values: Sequence[int]) -> List[int]:
    result_collection: List[int] = []
    position_counter: int = 0
    while position_counter < len(sequence_of_values):
        current_item: int = sequence_of_values[position_counter]
        if 0 < current_item:
            result_collection.append(current_item)
        position_counter += 1
    return result_collection