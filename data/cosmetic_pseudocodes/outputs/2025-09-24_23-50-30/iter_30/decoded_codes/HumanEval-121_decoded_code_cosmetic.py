from typing import List

def solution(array_of_numbers: List[int]) -> int:
    accumulator: int = 0
    pointer: int = 0
    while pointer < len(array_of_numbers):
        if (pointer % 2 == 0) and (array_of_numbers[pointer] % 2 == 1):
            accumulator += array_of_numbers[pointer]
        pointer += 1
    return accumulator