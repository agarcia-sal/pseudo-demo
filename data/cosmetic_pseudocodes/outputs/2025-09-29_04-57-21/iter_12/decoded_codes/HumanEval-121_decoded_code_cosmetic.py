from typing import List

def solution(list_of_integers: List[int]) -> int:
    total_sum: int = 0
    current_position: int = 0

    while current_position < len(list_of_integers):
        element: int = list_of_integers[current_position]
        if current_position % 2 != 1:  # Even indices (0-based)
            if element % 2 == 1:
                total_sum += element
        current_position += 1

    return total_sum