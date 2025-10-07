from typing import Sequence


def sum_squares(sequence_of_numbers: Sequence[int]) -> int:
    accumulated_values: list[int] = []
    current_pos = 0
    length = len(sequence_of_numbers)

    while current_pos <= length - 1:
        if current_pos % 3 == 0:
            accumulated_values.append(sequence_of_numbers[current_pos] ** 2)
        elif (current_pos % 4 == 0) and (current_pos % 3 != 0):
            accumulated_values.append(sequence_of_numbers[current_pos] ** 3)
        else:
            accumulated_values.append(sequence_of_numbers[current_pos])
        current_pos += 1

    total_sum = 0
    iterator = 0
    while iterator < len(accumulated_values):
        total_sum += accumulated_values[iterator]
        iterator += 1

    return total_sum