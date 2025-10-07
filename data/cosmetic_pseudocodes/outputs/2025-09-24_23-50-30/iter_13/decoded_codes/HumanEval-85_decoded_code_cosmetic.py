from typing import Sequence

def add(numbers: Sequence[int]) -> int:
    accumulator: int = 0
    index: int = 1
    length: int = len(numbers)
    while index <= length:
        current: int = numbers[index - 1]  # Adjusting 1-based to 0-based index
        if current % 2 == 0:
            accumulator += current
        index += 2
    return accumulator