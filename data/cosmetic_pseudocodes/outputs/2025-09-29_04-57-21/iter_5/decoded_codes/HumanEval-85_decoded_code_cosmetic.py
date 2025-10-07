from typing import List

def add(list_of_integers: List[int]) -> int:
    result: int = 0
    index: int = 0
    while index < len(list_of_integers):
        if list_of_integers[index] % 2 == 0:
            result += list_of_integers[index]
        index += 2
    return result