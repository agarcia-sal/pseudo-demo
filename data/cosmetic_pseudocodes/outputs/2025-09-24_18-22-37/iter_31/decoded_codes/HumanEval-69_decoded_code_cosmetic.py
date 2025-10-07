from typing import Sequence

def search(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = -1
    maximum_number: int = 0
    for element in sequence_of_numbers:
        if element > maximum_number:
            maximum_number = element
    count_array: list[int] = [0] * (maximum_number + 1)
    for item in sequence_of_numbers:
        count_array[item] += 1
    iterator_index: int = 1
    while iterator_index < len(count_array):
        current_frequency: int = count_array[iterator_index]
        if current_frequency >= iterator_index:
            accumulator = iterator_index
        iterator_index += 1
    return accumulator