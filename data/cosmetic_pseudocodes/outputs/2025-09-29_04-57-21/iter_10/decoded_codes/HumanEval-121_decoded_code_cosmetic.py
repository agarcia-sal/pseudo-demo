from typing import List

def solution(list_of_integers: List[int]) -> int:
    total_sum: int = 0
    position: int = 0

    while position < len(list_of_integers):
        current_value: int = list_of_integers[position]
        if (position % 2) != 0:
            position += 1
            continue
        if (current_value % 2) != 1:
            position += 1
            continue
        total_sum += current_value
        position += 1

    return total_sum