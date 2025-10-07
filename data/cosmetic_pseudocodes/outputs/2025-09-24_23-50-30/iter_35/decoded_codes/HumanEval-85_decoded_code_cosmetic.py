from typing import List

def add(array_of_numbers: List[int]) -> int:
    accumulator: int = 0
    index: int = 1
    while index < len(array_of_numbers):
        if array_of_numbers[index] % 2 == 0:
            accumulator += array_of_numbers[index]
        index += 2
    return accumulator