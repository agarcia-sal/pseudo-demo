from typing import List

def solution(list_of_integers: List[int]) -> int:
    accumulator: int = 0
    position: int = 0

    while position < len(list_of_integers):
        if not (position % 2 != 0 or list_of_integers[position] % 2 == 0):
            accumulator += list_of_integers[position]
        position += 1

    return accumulator