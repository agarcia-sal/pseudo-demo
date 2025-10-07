from typing import List

def search(arr: List[int]) -> int:
    if not arr:
        return -1  # Handle empty input gracefully
    max_val = max(arr)
    freq_array = [0] * (max_val + 1)
    for val in arr:
        freq_array[val] += 1
    result = -1
    for idx in range(1, len(freq_array)):
        if freq_array[idx] >= idx:
            result = idx
    return result