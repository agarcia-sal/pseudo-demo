from typing import List


def add(list_of_integers: List[int]) -> int:
    acc: int = 0
    idx: int = 1
    length: int = len(list_of_integers)
    while idx <= length:
        if list_of_integers[idx - 1] % 2 == 0:  # adjust index since pseudocode is 1-based
            acc += list_of_integers[idx - 1]
        idx += 2
    return acc