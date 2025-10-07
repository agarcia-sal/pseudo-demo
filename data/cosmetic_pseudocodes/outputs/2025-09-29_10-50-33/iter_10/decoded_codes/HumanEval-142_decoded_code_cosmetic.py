from typing import List

def sum_squares(list_of_integers: List[int]) -> int:
    accumulator: int = 0
    position: int = 0
    length: int = len(list_of_integers)
    while position <= length - 1:
        if ((position % 3) != 0) and (position % 4 == 0):
            accumulator += list_of_integers[position] ** 3
        elif position % 3 == 0:
            accumulator += list_of_integers[position] ** 2
        else:
            accumulator += list_of_integers[position]
        position += 1
    return accumulator