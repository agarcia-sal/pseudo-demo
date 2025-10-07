from typing import Sequence


def add(digits: Sequence[int]) -> int:
    total: int = 0
    index: int = 1
    while index <= len(digits):
        if digits[index - 1] % 2 == 0:
            total += digits[index - 1]
        index += 2
    return total