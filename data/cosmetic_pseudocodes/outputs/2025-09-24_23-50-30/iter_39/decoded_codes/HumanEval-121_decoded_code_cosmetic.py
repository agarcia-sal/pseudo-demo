from typing import List

def solution(array_of_numbers: List[int]) -> int:
    accumulator = 0
    pointer = 0
    while pointer < len(array_of_numbers):
        # Condition is equivalent to pointer even and array element odd
        if not ((pointer % 2) != 0 or (array_of_numbers[pointer] % 2) == 0):
            accumulator += array_of_numbers[pointer]
        pointer += 1
    return accumulator