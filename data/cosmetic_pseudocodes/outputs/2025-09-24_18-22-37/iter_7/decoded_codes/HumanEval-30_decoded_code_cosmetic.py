from typing import Sequence, List


def get_positive(sequence_of_values: Sequence[float]) -> List[float]:
    filtered_collection: List[float] = []
    position_index: int = 0
    while position_index < len(sequence_of_values):
        current_item = sequence_of_values[position_index]
        if current_item > 0:
            filtered_collection.append(current_item)
        position_index += 1
    return filtered_collection