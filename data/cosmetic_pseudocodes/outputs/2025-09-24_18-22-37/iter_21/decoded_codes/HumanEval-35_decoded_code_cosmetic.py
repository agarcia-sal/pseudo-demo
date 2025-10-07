from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError("max_element() arg is an empty sequence")
    current_maximum: T = sequence[0]
    index_pointer: int = 0
    while index_pointer < len(sequence):
        candidate: T = sequence[index_pointer]
        if candidate > current_maximum:
            current_maximum = candidate
        index_pointer += 1
    return current_maximum