from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    max_val = max(sequence_of_numbers, default=0)
    count_array = [0] * (max_val + 1)
    iterator = 0
    while iterator < len(sequence_of_numbers):
        current_element = sequence_of_numbers[iterator]
        count_array[current_element] += 1
        iterator += 1

    result = -1
    position = 1
    while position < len(count_array):
        current_frequency = count_array[position]
        if current_frequency >= position:
            result = position
        position += 1

    return result