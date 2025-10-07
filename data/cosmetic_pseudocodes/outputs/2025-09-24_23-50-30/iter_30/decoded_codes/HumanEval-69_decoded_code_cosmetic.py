from typing import List

def search(collection_of_numbers: List[int]) -> int:
    if not collection_of_numbers:
        return -1  # handle empty input gracefully

    max_val: int = max(collection_of_numbers)
    counts: List[int] = [0] * (max_val + 1)

    idx: int = 0
    while idx < len(collection_of_numbers):
        val: int = collection_of_numbers[idx]
        counts[val] += 1
        idx += 1

    result: int = -1
    pos: int = 1
    while pos <= len(counts) - 1:
        if counts[pos] >= pos:
            result = pos
            break
        pos += 1

    return result