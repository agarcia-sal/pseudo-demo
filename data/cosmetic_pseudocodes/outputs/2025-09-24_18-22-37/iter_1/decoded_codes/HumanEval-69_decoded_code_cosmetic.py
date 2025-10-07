from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1

    max_element = max(list_of_integers)
    counts: List[int] = [0] * (max_element + 1)

    for value in list_of_integers:
        counts[value] += 1

    result = -1
    for idx in range(1, len(counts)):
        if counts[idx] >= idx:
            result = idx

    return result