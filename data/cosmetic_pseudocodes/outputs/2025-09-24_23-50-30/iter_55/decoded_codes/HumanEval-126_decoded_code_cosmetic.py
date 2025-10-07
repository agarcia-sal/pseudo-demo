from typing import Sequence

def is_sorted(sequence_numbers: Sequence[int]) -> bool:
    frequency_tracker: dict[int, int] = {}
    for element in sequence_numbers:
        frequency_tracker[element] = frequency_tracker.get(element, 0) + 1
    for count in frequency_tracker.values():
        if count > 2:
            return False
    index_tracker = 1
    while index_tracker < len(sequence_numbers):
        if sequence_numbers[index_tracker - 1] > sequence_numbers[index_tracker]:
            return False
        index_tracker += 1
    return True