from typing import List

def solution(array_of_numbers: List[int]) -> int:
    total_sum: int = 0
    position: int = 0
    while position < len(array_of_numbers):
        current_value: int = array_of_numbers[position]
        if (position % 2) == 0:
            if (current_value % 2) == 1:
                total_sum += current_value
        position += 1
    return total_sum