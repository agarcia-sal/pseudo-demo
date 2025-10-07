from typing import Sequence


def solution(sequence_of_numbers: Sequence[int]) -> int:
    def helper(position: int, accumulator: int) -> int:
        if position >= len(sequence_of_numbers):
            return accumulator
        element = sequence_of_numbers[position]
        # Add element to accumulator only if position is even and element is odd
        increment = element if (position % 2 == 0 and element % 2 == 1) else 0
        return helper(position + 1, accumulator + increment)

    return helper(0, 0)