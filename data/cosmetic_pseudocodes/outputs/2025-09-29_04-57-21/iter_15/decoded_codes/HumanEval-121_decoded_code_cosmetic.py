from typing import List

def solution(list_of_integers: List[int]) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(list_of_integers):
        element: int = list_of_integers[position]
        if not (position % 2 != 0) and (element % 2 == 1):
            accumulator += element
        position += 1
    return accumulator