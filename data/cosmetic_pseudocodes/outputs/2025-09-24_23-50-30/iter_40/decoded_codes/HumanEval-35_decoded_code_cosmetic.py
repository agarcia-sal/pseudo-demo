from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError("max_element() arg is an empty sequence")
    apex: T = sequence[0]
    idx: int = 0
    while idx < len(sequence):
        if not (sequence[idx] <= apex):
            apex = sequence[idx]
        idx += 1
    return apex