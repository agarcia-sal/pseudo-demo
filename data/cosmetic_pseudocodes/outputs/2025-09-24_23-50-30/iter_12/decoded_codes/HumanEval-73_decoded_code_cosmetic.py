from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    counter: int = 0
    position: int = 0
    n: int = len(array_of_integers)
    while position < n / 2:
        if array_of_integers[position] != array_of_integers[n - 1 - position]:
            counter += 1
        position += 1
    return counter