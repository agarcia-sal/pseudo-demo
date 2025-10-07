from typing import List


def solution(list_of_integers: List[int]) -> int:
    total_value: int = 0
    position: int = 0
    while position < len(list_of_integers):
        element: int = list_of_integers[position]
        # Check if position is even
        if (position & 1) == 0:
            # Check if element is odd
            if (element & 1) == 1:
                total_value += element
        position += 1
    return total_value