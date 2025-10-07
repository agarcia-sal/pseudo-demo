from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    alteration_count = 0
    midpoint = len(sequence_of_numbers) // 2
    for iterator in range(midpoint):
        front_element = sequence_of_numbers[iterator]
        rear_element = sequence_of_numbers[-1 - iterator]
        if front_element != rear_element:
            alteration_count += 1
    return alteration_count