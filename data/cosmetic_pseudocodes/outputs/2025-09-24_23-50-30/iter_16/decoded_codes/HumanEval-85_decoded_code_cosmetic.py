from typing import List

def add(list_of_integers: List[int]) -> int:
    accumulator: int = 0
    current_index: int = 1
    while current_index <= len(list_of_integers):
        if list_of_integers[current_index - 1] % 2 == 0:
            accumulator += list_of_integers[current_index - 1]
        current_index += 2
    return accumulator