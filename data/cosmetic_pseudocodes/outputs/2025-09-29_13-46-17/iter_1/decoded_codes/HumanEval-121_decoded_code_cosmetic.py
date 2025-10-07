from typing import List

def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    for index, value in enumerate(list_of_integers):
        if index % 2 == 0 and value % 2 == 1:
            total += value
    return total