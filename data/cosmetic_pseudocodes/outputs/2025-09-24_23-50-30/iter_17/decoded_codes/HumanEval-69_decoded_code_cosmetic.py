from collections import defaultdict
from typing import List

def search(array_of_numbers: List[int]) -> int:
    counts_map: defaultdict[int, int] = defaultdict(int)
    for element in array_of_numbers:
        counts_map[element] += 1
    result: int = -1
    keys_list: List[int] = list(counts_map.keys())
    max_key: int = 0
    for key in keys_list:
        if key > max_key:
            max_key = key
    for candidate in range(max_key, 0, -1):
        if counts_map[candidate] >= candidate:
            result = candidate
            break
    return result