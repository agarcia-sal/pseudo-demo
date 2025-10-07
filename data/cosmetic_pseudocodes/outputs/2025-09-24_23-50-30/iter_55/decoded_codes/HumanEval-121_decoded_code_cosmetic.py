from typing import Sequence


def solution(collection_of_numbers: Sequence[int]) -> int:
    def helper(position: int, accumulator: int) -> int:
        if position == len(collection_of_numbers):
            return accumulator
        element = collection_of_numbers[position]
        updated_accumulator = accumulator if (position % 2 != 0 or element % 2 != 1) else accumulator + element
        return helper(position + 1, updated_accumulator)

    return helper(0, 0)