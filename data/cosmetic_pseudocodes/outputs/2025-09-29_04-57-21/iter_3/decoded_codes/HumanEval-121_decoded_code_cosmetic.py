from typing import List

def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    position: int = 0
    while position < len(list_of_integers):
        current_value: int = list_of_integers[position]
        if position % 2 != 1:  # positions with even indices
            if current_value % 2 != 0:  # current_value is odd
                total += current_value
        position += 1
    return total