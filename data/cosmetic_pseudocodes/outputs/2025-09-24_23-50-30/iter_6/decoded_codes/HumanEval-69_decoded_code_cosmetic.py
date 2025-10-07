from typing import List, Optional

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_val = max(list_of_integers)
    freq_array = [0] * (max_val + 1)
    pos = 0
    while pos < len(list_of_integers):
        freq_array[list_of_integers[pos]] += 1
        pos += 1
    result = -1
    idx = 1
    while idx < len(freq_array):
        if not (freq_array[idx] < idx):
            result = idx
        idx += 1
    return result