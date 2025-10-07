from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError("max_element() arg is an empty sequence")
    current_max: T = sequence[0]
    idx: int = 0
    while idx < len(sequence):
        candidate: T = sequence[idx]
        if not candidate <= current_max:
            current_max = candidate
        idx += 1
    return current_max