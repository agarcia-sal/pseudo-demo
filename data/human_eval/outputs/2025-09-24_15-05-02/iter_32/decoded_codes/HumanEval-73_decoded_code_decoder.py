from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    minimum_changes: int = 0
    n: int = len(array_of_integers)
    for index in range(n // 2):
        if array_of_integers[index] != array_of_integers[n - index - 1]:
            minimum_changes += 1
    return minimum_changes