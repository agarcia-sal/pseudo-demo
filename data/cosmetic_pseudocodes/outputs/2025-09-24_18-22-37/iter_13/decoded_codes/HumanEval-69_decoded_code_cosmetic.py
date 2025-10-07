from typing import List

def search(numbers: List[int]) -> int:
    max_num = max(numbers, default=-1)
    counts: List[int] = [0] * (max_num + 1)
    iterator = 0
    while iterator < len(numbers):
        element = numbers[iterator]
        prev_count = counts[element]
        next_count = prev_count + 1
        counts[element] = next_count
        iterator += 1
    result = -1
    pos = 1
    while pos <= len(counts) - 1:
        if counts[pos] >= pos:
            result = pos
        pos += 1
    return result