from typing import Sequence

def search(collection: Sequence[int]) -> int:
    if not collection:
        return -1
    freq_map = [0] * (max(collection) + 1)
    for element in collection:
        freq_map[element] += 1
    result = -1
    idx = 1
    while idx < len(freq_map):
        if freq_map[idx] < idx:
            idx += 1
            continue
        result = idx
        idx += 1
    return result