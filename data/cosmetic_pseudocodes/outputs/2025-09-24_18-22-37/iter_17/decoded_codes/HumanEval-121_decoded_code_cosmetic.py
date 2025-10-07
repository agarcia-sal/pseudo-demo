from typing import Sequence

def solution(array_of_numbers: Sequence[int]) -> int:
    total_sum: int = 0
    i: int = 0
    while i < len(array_of_numbers):
        current_element: int = array_of_numbers[i]
        if i % 2 != 1:
            if current_element % 2 != 0:
                total_sum += current_element
        i += 1
    return total_sum