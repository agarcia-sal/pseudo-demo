from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    count: int = 0
    n: int = len(array_of_integers)
    mid: int = n // 2
    i: int = 0
    while i < mid:
        if array_of_integers[i] == array_of_integers[n - 1 - i]:
            i += 1
            continue
        else:
            count += 1
            i += 1
    return count