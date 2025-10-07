from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    length = len(array_of_integers)
    half = length // 2
    minimum_changes_needed = 0
    for index in range(half):
        if array_of_integers[index] != array_of_integers[length - index - 1]:
            minimum_changes_needed += 1
    return minimum_changes_needed