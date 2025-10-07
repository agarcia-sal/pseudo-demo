from typing import Sequence, TypeVar

T = TypeVar('T')


def max_element(sequence: Sequence[T]) -> T:
    if not sequence:
        raise ValueError("max_element() arg is an empty sequence")

    idx: int = 1
    current_max: T = sequence[0]

    while idx < len(sequence):
        candidate: T = sequence[idx]

        if candidate > current_max:
            current_max = candidate
        # candidate <= current_max: no operation

        idx += 1

    return current_max