from typing import List

def solution(list_of_integers: List[int]) -> int:
    acc: int = 0
    cursor: int = 0
    while cursor < len(list_of_integers):
        element: int = list_of_integers[cursor]
        if not ((cursor % 2 != 0) or (element % 2 != 1)):
            acc += element
        cursor += 1
    return acc