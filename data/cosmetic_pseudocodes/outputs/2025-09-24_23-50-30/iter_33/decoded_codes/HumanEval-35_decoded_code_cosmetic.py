from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(input_sequence: Sequence[T]) -> T:
    def helper(iterator: Sequence[T], current_max: T) -> T:
        if not iterator:
            return current_max
        candidate = iterator[0]
        next_max = candidate if candidate > current_max else current_max
        return helper(iterator[1:], next_max)

    if not input_sequence:
        raise ValueError("max_element() arg is an empty sequence")
    return helper(input_sequence, input_sequence[0])