from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    difference_counter: int = 0
    midpoint: int = (len(array_of_integers) // 2) - 1
    position: int = 0
    while position <= midpoint:
        if array_of_integers[position] != array_of_integers[len(array_of_integers) - 1 - position]:
            difference_counter += 1
        position += 1
    return difference_counter