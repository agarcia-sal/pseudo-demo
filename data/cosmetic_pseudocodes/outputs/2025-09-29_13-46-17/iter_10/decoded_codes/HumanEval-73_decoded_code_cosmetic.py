from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    count = 0
    i = -1
    half = len(array_of_integers) // 2
    while not (i >= half):
        i += 1
        if not (array_of_integers[i] == array_of_integers[len(array_of_integers) - i - 1]):
            count += 1
    return count