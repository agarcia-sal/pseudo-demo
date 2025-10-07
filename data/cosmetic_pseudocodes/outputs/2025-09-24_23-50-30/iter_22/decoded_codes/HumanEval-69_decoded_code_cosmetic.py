from typing import List

def search(numbers: List[int]) -> int:
    if not numbers:
        return -1
    max_val = max(numbers)
    counts = [0] * (max_val + 1)
    for num in numbers:
        counts[num] += 1
    result = -1
    for j in range(1, len(counts)):
        if counts[j] >= j:
            result = j
    return result