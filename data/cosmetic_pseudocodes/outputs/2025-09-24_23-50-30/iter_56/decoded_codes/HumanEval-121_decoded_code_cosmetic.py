from typing import List

def solution(array_of_numbers: List[int]) -> int:
    accumulator: int = 0
    iterator: int = 0
    length: int = len(array_of_numbers)
    while iterator < length:
        element: int = array_of_numbers[iterator]
        if (iterator - 2 * (iterator // 2) == 0) and (element - 2 * (element // 2) == 1):
            accumulator += element
        iterator += 1
    return accumulator