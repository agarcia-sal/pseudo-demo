from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Sequence[T]) -> List[T]:
    frequency_map = Counter(sequence_of_values)
    filtered_list: List[T] = []
    iteration_index = 0
    while iteration_index < len(sequence_of_values):
        current_item = sequence_of_values[iteration_index]
        if frequency_map[current_item] <= 1:
            filtered_list.append(current_item)
        iteration_index += 1
    return filtered_list