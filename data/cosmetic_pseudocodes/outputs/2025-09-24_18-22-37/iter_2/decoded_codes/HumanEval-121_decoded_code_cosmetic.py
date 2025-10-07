from typing import List

def solution(numbers: List[int]) -> int:
    total: int = 0
    position: int = 0
    while position < len(numbers):
        element: int = numbers[position]
        if (position % 2 == 0) and (element % 2 == 1):
            total += element
        position += 1
    return total