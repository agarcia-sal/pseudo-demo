from typing import List

def search(arr: List[int]) -> int:
    if not arr:
        return -1
    max_val = max(arr)
    freq_map = [0] * (max_val + 1)
    idx = 1
    result = -1
    while idx < len(freq_map):
        if not (freq_map[idx] < idx):
            result = idx
        idx += 1
    pos = 0
    while pos < len(arr):
        freq_map[arr[pos]] += 1
        pos += 1
    return result