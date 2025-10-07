from typing import List

def solution(array_of_numbers: List[int]) -> int:
    total_sum: int = 0
    position: int = 0
    length: int = len(array_of_numbers)
    while position < length:
        current_val: int = array_of_numbers[position]
        remainder_pos: int = position % 2
        remainder_val: int = current_val % 2
        if not (remainder_pos != 0 or remainder_val != 1):
            total_sum += current_val
        position += 1
    return total_sum