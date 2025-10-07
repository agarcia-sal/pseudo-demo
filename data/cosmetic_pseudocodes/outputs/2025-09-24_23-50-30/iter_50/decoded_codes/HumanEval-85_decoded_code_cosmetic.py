from typing import List

def add(list_of_integers: List[int]) -> int:
    total: int = 0
    index_tracker: int = 1
    while index_tracker <= len(list_of_integers):
        if list_of_integers[index_tracker - 1] % 2 == 0:
            total += list_of_integers[index_tracker - 1]
        index_tracker += 2
    return total