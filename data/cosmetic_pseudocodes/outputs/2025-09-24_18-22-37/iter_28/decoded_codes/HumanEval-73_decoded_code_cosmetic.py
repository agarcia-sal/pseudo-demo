from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    difference_count = 0
    total_length = len(sequence_of_numbers)
    midpoint = (total_length // 2) - 1  # integer division and minus one for midpoint index
    position = 0
    while position <= midpoint:
        front_value = sequence_of_numbers[position]
        back_index = total_length - position - 1
        back_value = sequence_of_numbers[back_index]
        if front_value != back_value:
            flag_increment = True
        else:
            flag_increment = False
        if flag_increment:
            difference_count += 1
        position += 1
    return difference_count