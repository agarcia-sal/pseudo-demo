from typing import List

def search(arr: List[int]) -> int:
    if not arr:
        return -1
    max_val = max(arr)
    freq = [0] * (max_val + 1)
    res = -1
    for x in arr:
        freq[x] += 1
    for j in range(1, len(freq)):
        if freq[j] >= j:
            res = j
    return res