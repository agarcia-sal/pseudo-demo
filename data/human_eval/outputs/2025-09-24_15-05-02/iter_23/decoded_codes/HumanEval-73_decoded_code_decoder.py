from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    changes_needed: int = 0
    length: int = len(array_of_integers)
    half_length: int = length // 2
    for index in range(half_length):
        if array_of_integers[index] != array_of_integers[length - index - 1]:
            changes_needed += 1
    return changes_needed