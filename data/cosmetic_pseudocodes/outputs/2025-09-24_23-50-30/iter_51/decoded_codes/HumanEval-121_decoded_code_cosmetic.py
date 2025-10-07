from typing import Sequence


def solution(collection: Sequence[int]) -> int:
    def helper(sequence: Sequence[int], position: int, accumulator: int) -> int:
        if position == len(sequence):
            return accumulator
        current_element = sequence[position]
        updated_accumulator = accumulator + current_element if position % 2 == 0 and current_element % 2 == 1 else accumulator
        return helper(sequence, position + 1, updated_accumulator)

    return helper(collection, 0, 0)