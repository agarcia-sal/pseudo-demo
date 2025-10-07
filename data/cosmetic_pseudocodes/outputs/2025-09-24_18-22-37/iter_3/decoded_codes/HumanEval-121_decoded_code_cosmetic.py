from typing import List


def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    position: int = 0
    length: int = len(list_of_integers)

    while position < length:
        element: int = list_of_integers[position]
        if position % 2 != 1:
            if element % 2 != 0:
                total += element
        position += 1

    return total