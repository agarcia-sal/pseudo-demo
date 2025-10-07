from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    def locate_maximum(current_index: int, current_maximum: T) -> T:
        if current_index >= len(sequence):
            return current_maximum
        candidate = sequence[current_index]
        updated_maximum = current_maximum if candidate <= current_maximum else candidate
        return locate_maximum(current_index + 1, updated_maximum)
    return locate_maximum(0, sequence[0])