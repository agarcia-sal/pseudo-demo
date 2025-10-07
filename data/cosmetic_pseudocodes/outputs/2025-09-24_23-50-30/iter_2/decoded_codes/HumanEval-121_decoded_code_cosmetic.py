from typing import List


def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    index: int = 0
    while not (index >= len(list_of_integers)):
        # Include element if index is even AND element is odd
        if not (index % 2 != 0 or list_of_integers[index] % 2 == 0):
            total += list_of_integers[index]
        index += 1
    return total