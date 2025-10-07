from typing import List

def search(array_of_nums: List[int]) -> int:
    if not array_of_nums:
        return -1  # handle empty input gracefully

    max_val = max(array_of_nums)
    counts: List[int] = [0] * (max_val + 1)

    for val in array_of_nums:
        counts[val] += 1

    res = -1
    for j in range(1, len(counts)):
        if counts[j] >= j:
            res = j

    return res