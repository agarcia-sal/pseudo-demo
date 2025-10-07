from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    difference_count: int = 0
    halving_limit: int = len(array_of_integers) // 2 - 1
    position: int = 0
    while position <= halving_limit:
        if array_of_integers[position] != array_of_integers[len(array_of_integers) - 1 - position]:
            difference_count += 1
        position += 1
    return difference_count