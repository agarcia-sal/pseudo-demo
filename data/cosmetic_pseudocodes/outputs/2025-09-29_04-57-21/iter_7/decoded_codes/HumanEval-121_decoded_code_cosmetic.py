from typing import Sequence

def solution(numbers_collection: Sequence[int]) -> int:
    accumulator: int = 0
    position: int = 0

    while position < len(numbers_collection):
        current_value: int = numbers_collection[position]

        # Condition equivalent to NOT ((position is odd) OR (current_value is odd))
        # i.e., both position and current_value must be even
        if not ((position % 2 != 0) or (current_value % 2 != 1)):
            accumulator += current_value

        position += 1

    return accumulator