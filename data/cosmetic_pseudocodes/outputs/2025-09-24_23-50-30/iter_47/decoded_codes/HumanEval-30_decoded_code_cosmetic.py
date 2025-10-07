from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=float)  # Assuming numerical types that support > 0

def get_positive(sequence_of_values: Sequence[T]) -> List[T]:
    idx: int = 0
    filtered_collection: List[T] = []
    while idx < len(sequence_of_values):
        if sequence_of_values[idx] > 0:
            filtered_collection.append(sequence_of_values[idx])
        idx += 1
    return filtered_collection