from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=float)  # Assuming sequence_of_values contains floats or comparable numeric types

def get_positive(sequence_of_values: Sequence[T]) -> List[T]:
    filtered_collection: List[T] = []
    index_holder: int = 0

    while index_holder < len(sequence_of_values):
        if not (sequence_of_values[index_holder] <= 0):
            filtered_collection.append(sequence_of_values[index_holder])
        index_holder += 1

    return filtered_collection