from typing import List


def add(list_of_integers: List[int]) -> int:
    total: int = 0
    index: int = 1
    while index <= len(list_of_integers):
        if list_of_integers[index - 1] % 2 == 0:
            total += list_of_integers[index - 1]
        index += 2
    return total