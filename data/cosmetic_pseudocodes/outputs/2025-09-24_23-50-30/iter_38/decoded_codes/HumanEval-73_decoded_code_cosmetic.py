from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    count = 0
    length = len(sequence_of_numbers)
    for position in range(length // 2):
        if sequence_of_numbers[position] != sequence_of_numbers[length - position - 1]:
            count += 1
    return count