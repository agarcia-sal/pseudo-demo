from typing import List

def search(array_of_numbers: List[int]) -> int:
    if not array_of_numbers:
        return -1
    counts = [0] * (max(array_of_numbers) + 1)
    pos = 0
    while pos < len(array_of_numbers):
        current_num = array_of_numbers[pos]
        counts[current_num] += 1
        pos += 1

    result = -1
    idx = 1
    while idx <= len(counts) - 1:
        if not (counts[idx] < idx):
            result = idx
        idx += 1

    return result