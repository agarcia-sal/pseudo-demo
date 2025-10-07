from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    def helper(idx: int, current_max: T) -> T:
        if idx < len(sequence):
            if sequence[idx] > current_max:
                return helper(idx + 1, sequence[idx])
            else:
                return helper(idx + 1, current_max)
        else:
            return current_max

    if not sequence:
        raise ValueError("max_element() arg is an empty sequence")
    return helper(0, sequence[0])