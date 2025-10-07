from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_element = max(list_of_integers)
    counts_array: List[int] = [0] * (max_element + 1)
    for element in list_of_integers:
        counts_array[element] += 1
    result = -1
    idx = 1
    while idx < len(counts_array):
        if counts_array[idx] >= idx:
            result = idx
        idx += 1
    return result