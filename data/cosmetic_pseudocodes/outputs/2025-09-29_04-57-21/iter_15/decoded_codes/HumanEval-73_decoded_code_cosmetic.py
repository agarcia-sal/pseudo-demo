from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    adjustments = 0
    length = len(array_of_integers)
    for position in range(length // 2):
        if array_of_integers[position] != array_of_integers[length - 1 - position]:
            adjustments += 1
    return adjustments