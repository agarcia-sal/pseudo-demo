from typing import List

def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    i: int = 0
    while i < len(list_of_integers):
        if i % 2 == 0:
            if list_of_integers[i] % 2 == 1:
                total += list_of_integers[i]
        i += 1
    return total