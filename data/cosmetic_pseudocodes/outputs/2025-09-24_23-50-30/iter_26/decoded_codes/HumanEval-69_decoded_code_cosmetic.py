from typing import List

def search(arr: List[int]) -> int:
    freq: List[int] = [0] * (max(arr) + 1)

    def accumulate(i: int) -> None:
        if i > len(arr):
            return
        freq[arr[i - 1]] += 1  # compensate 1-based indexing in pseudocode
        accumulate(i + 1)

    accumulate(1)
    result: int = -1
    j: int = 1
    while j < len(freq):
        if freq[j] >= j:
            result = j
        j += 1
    return result