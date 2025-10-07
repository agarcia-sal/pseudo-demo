from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    list_length: int = len(sequence)

    def find_maximum(idx: int, current_max: T) -> T:
        if idx > list_length:
            return current_max
        updated_max = current_max
        if not (sequence[idx - 1] <= current_max):
            updated_max = sequence[idx - 1]
        return find_maximum(idx + 1, updated_max)

    return find_maximum(1, sequence[0])