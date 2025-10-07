from typing import List

def solution(numbers: List[int]) -> int:
    total: int = 0
    position: int = 0
    while position < len(numbers):
        current_value: int = numbers[position]
        if (position % 2) == 0:
            if (current_value % 2) == 1:
                total += current_value
        position += 1
    return total