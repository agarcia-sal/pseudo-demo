from typing import List

def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    for idx in range(len(list_of_integers)):
        value = list_of_integers[idx]
        if (idx % 2 == 0) and (value % 2 == 1):
            total += value
    return total