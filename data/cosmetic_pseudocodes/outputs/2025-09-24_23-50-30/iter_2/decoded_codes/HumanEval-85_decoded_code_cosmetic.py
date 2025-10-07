from typing import List

def add(list_of_integers: List[int]) -> int:
    total: int = 0
    idx: int = 2
    while idx < len(list_of_integers):
        if list_of_integers[idx] % 2 == 0:
            total += list_of_integers[idx]
        idx += 2
    return total