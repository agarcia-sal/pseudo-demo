from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    if not sequence_of_numbers:
        return -1
    max_value = max(sequence_of_numbers)
    counts_array = [0] * (max_value + 1)
    iterator_var = 0
    while iterator_var < len(sequence_of_numbers):
        current_element = sequence_of_numbers[iterator_var]
        current_frequency = counts_array[current_element]
        updated_frequency = current_frequency + 1
        counts_array[current_element] = updated_frequency
        iterator_var += 1

    result_value = -1
    position_var = 1
    while position_var < len(counts_array):
        current_count = counts_array[position_var]
        if current_count >= position_var:
            result_value = position_var
        position_var += 1

    return result_value