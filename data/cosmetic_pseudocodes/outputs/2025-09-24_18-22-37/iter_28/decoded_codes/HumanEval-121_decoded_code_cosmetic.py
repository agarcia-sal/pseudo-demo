from typing import List

def solution(array_of_numbers: List[int]) -> int:
    total: int = 0
    position: int = 0
    length: int = len(array_of_numbers)
    while position < length:
        element: int = array_of_numbers[position]
        if position % 2 != 0:
            # skip processing when position is odd
            position += 1
            continue
        if element % 2 != 1:
            # skip processing when element is not odd
            position += 1
            continue
        sum_component: int = element
        total += sum_component
        position += 1
    return total