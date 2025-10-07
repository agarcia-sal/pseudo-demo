from typing import List

def solution(list_of_integers: List[int]) -> int:
    return sum(x for idx, x in enumerate(list_of_integers) if idx % 2 == 0 and x % 2 == 1)