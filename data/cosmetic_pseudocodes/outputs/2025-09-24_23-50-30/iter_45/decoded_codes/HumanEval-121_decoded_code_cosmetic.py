from typing import List

def solution(input_array: List[int]) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator < len(input_array):
        if not ((iterator % 2 == 1) or (input_array[iterator] % 2 == 0)):
            accumulator += input_array[iterator]
        iterator += 1
    return accumulator