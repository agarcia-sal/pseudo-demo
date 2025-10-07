from typing import Sequence, List


def get_positive(sequence_of_values: Sequence[float]) -> List[float]:
    filtered_collection: List[float] = []
    position: int = 0
    while position < len(sequence_of_values):
        current_item: float = sequence_of_values[position]
        if not (current_item <= 0):
            filtered_collection.append(current_item)
        position += 1
    return filtered_collection