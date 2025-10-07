from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    max_value = max(sequence_of_numbers, default=-1)
    tally = [0] * (max_value + 1)
    for element in sequence_of_numbers:
        tally[element] += 1
    result_holder = -1
    position_tracker = 1
    while position_tracker < len(tally):
        if not (tally[position_tracker] < position_tracker):
            result_holder = position_tracker
        position_tracker += 1
    return result_holder