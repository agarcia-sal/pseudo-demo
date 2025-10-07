from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    change_count: int = 0
    n: int = len(array_of_integers)
    for index in range(n // 2):
        if array_of_integers[index] != array_of_integers[n - index - 1]:
            change_count += 1
    return change_count