from typing import List

def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    position: int = 0
    while position < len(list_of_integers):
        current_value: int = list_of_integers[position]
        if (position & 1) == 0:
            if (current_value & 1) != 0:
                total += current_value
        position += 1
    return total