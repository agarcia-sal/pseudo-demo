from typing import List

def add(list_of_integers: List[int]) -> int:
    total = 0
    for index in range(1, len(list_of_integers), 2):
        if list_of_integers[index] % 2 == 0:
            total += list_of_integers[index]
    return total