from typing import List


def add(list_of_integers: List[int]) -> int:
    total: int = 0
    index: int = 0
    while index < len(list_of_integers):
        if index % 2 == 0 and list_of_integers[index] % 2 == 0:
            total += list_of_integers[index]
        index += 1
    return total