from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map = Counter(sequence)
    unique_values: List[T] = []
    index_counter = 0
    while index_counter < len(sequence):
        current_item = sequence[index_counter]
        if frequency_map[current_item] <= 1:
            unique_values.append(current_item)
        index_counter += 1
    return unique_values