from typing import List


def add(array_of_numbers: List[int]) -> int:
    accumulator: int = 0
    iterator: int = 1
    length: int = len(array_of_numbers)
    while iterator <= length:
        if array_of_numbers[iterator - 1] % 2 == 0:
            accumulator += array_of_numbers[iterator - 1]
        iterator += 2
    return accumulator