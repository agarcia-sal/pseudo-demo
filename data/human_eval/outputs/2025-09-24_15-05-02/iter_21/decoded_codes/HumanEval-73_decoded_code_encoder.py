from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    changes_needed: int = 0
    n: int = len(array_of_integers)
    for index in range(n // 2):
        if array_of_integers[index] != array_of_integers[n - index - 1]:
            changes_needed += 1
    return changes_needed