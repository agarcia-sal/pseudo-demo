from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1

    max_val = max(list_of_integers)
    counts = [0] * (max_val + 1)

    for element in list_of_integers:
        counts[element] += 1

    result = -1
    idx = 1
    while idx < len(counts):
        if not (counts[idx] < idx):
            result = idx
        idx += 1

    return result