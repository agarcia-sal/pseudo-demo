from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    differences = 0
    n = len(array_of_integers)
    half_point = n // 2  # integer division to get midpoint
    for i in range(half_point):
        if array_of_integers[i] != array_of_integers[n - 1 - i]:
            differences += 1
    return differences