from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    counter_variable: int = 0
    counter_tracker: int = 0
    length: int = len(sequence_of_numbers)
    half_length: int = length // 2
    while counter_tracker < half_length:
        if sequence_of_numbers[counter_tracker] != sequence_of_numbers[length - counter_tracker - 1]:
            counter_variable += 1
        counter_tracker += 1
    return counter_variable