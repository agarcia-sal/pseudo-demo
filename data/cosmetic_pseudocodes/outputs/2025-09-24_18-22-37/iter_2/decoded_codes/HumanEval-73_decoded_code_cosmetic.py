from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    count_of_diff = 0
    n = len(array_of_integers)
    midpoint = n // 2
    for i in range(midpoint):
        if array_of_integers[i] != array_of_integers[n - i - 1]:
            count_of_diff += 1
    return count_of_diff