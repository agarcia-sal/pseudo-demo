from typing import List


def add(list_of_integers: List[int]) -> int:
    total: int = 0
    current_index: int = 1
    while current_index < len(list_of_integers):
        number: int = list_of_integers[current_index]
        if number % 2 == 0:
            total += number
        current_index += 2
    return total