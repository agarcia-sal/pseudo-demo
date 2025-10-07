from typing import Sequence

def search(input_collection: Sequence[int]) -> int:
    if not input_collection:
        return -1  # Handle empty input gracefully
    max_value = max(input_collection)
    counts = [0] * (max_value + 1)
    idx = 0
    length = len(input_collection)
    while idx < length:
        val = input_collection[idx]
        counts[val] += 1
        idx += 1
    result_candidate = -1
    check_idx = 1
    counts_length = len(counts)
    while check_idx < counts_length:
        current_frequency = counts[check_idx]
        if not (current_frequency < check_idx):
            result_candidate = check_idx
        check_idx += 1
    return result_candidate