from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(input_sequence: Sequence[T]) -> T:
    def finder(sequence: Sequence[T], idx: int, current_max: T) -> T:
        if idx == len(sequence):
            return current_max
        if sequence[idx] > current_max:
            return finder(sequence, idx + 1, sequence[idx])
        else:
            return finder(sequence, idx + 1, current_max)
    if not input_sequence:
        raise ValueError("max_element() arg is an empty sequence")
    return finder(input_sequence, 1, input_sequence[0])