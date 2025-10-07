from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_val = max(list_of_integers)
    counts = {i: 0 for i in range(max_val + 1)}
    for element in list_of_integers:
        counts[element] += 1
    result = -1
    keys = sorted(k for k in counts if k > 0)
    for key in keys:
        if counts[key] >= key:
            result = key
    return result