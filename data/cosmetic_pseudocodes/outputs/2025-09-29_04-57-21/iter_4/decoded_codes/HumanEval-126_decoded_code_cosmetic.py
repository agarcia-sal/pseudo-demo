from typing import Sequence

def is_sorted(sequence_of_values: Sequence[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for index in range(len(sequence_of_values)):
        current_val = sequence_of_values[index]
        frequency_map[current_val] = frequency_map.get(current_val, 0) + 1
    for element in sequence_of_values:
        if frequency_map[element] > 2:
            return False
    position = 1
    while position < len(sequence_of_values):
        previous_value = sequence_of_values[position - 1]
        current_value = sequence_of_values[position]
        if not (previous_value <= current_value):
            return False
        position += 1
    return True