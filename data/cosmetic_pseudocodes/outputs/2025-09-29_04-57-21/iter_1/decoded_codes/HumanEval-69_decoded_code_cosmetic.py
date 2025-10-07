from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_integer = max(list_of_integers)
    counts: List[int] = [0] * (max_integer + 1)
    for integer in list_of_integers:
        counts[integer] += 1
    result = -1
    for i in range(1, len(counts)):
        if counts[i] >= i:
            result = i
    return result