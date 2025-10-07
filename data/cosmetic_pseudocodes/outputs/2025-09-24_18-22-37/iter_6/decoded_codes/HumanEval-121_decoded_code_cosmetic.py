from typing import List

def solution(array_of_numbers: List[int]) -> int:
    total: int = 0
    position: int = 0
    while position < len(array_of_numbers):
        if position % 2 == 0:
            current_value: int = array_of_numbers[position]
            if current_value % 2 == 1:
                total += current_value
        position += 1
    return total