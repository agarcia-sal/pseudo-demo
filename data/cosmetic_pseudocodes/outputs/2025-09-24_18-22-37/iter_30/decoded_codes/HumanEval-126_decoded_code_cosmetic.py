from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T', bound='object')

def is_sorted(sequence_of_values: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for element in sequence_of_values:
        frequency_map[element] = 0
    idx = 0
    length = len(sequence_of_values)
    while idx < length:
        current_value = sequence_of_values[idx]
        frequency_map[current_value] += 1
        idx += 1
    for key in sequence_of_values:
        if frequency_map[key] > 2:
            return False
    pos = 1
    while pos <= length - 1:
        previous_value = sequence_of_values[pos - 1]
        current_value = sequence_of_values[pos]
        if not (previous_value <= current_value):
            return False
        pos += 1
    return True