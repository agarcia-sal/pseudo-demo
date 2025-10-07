from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=float)  # Assuming elements comparable to 0

def get_positive(sequence: Sequence[T]) -> List[T]:
    accumulator: List[T] = []
    current_index = 0

    while current_index < len(sequence):
        if not (sequence[current_index] <= 0):
            accumulator.append(sequence[current_index])
        current_index += 1

    return accumulator