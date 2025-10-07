from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    if not sequence_of_numbers:
        return -1
    max_value = max(sequence_of_numbers)
    counts = [0] * (max_value + 1)
    for element in sequence_of_numbers:
        counts[element] += 1
    result = -1
    for idx in range(1, len(counts)):
        if counts[idx] >= idx:
            result = idx
    return result