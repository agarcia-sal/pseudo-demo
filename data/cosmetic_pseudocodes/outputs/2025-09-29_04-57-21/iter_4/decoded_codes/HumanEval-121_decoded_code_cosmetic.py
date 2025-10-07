from typing import Iterable


def solution(numbers_collection: Iterable[int]) -> int:
    accumulator: int = 0
    position: int = 0

    while position < len(numbers_collection):  # type: ignore
        candidate = numbers_collection[position]  # type: ignore
        # Add candidate if position is even and candidate is odd
        if not ((position % 2) != 0 or (candidate % 2) != 1):
            accumulator += candidate
        position += 1

    return accumulator