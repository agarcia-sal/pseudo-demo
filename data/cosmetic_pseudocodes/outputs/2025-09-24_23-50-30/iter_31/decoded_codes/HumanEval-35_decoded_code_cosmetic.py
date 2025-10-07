from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence_container: Sequence[T]) -> T:
    if not sequence_container:
        raise ValueError("max_element() arg is an empty sequence")
    cursor: int = 0
    candidate_max: T = sequence_container[cursor]
    while cursor < len(sequence_container):
        current_value: T = sequence_container[cursor]
        if current_value > candidate_max:
            candidate_max = current_value
        cursor += 1
    return candidate_max