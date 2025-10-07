from typing import Sequence, List, TypeVar
from collections import Counter

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Sequence[T]) -> List[T]:
    frequency_map = Counter(sequence_of_values)
    output_collection: List[T] = []
    idx = 0
    while idx < len(sequence_of_values):
        current_entry = sequence_of_values[idx]
        if frequency_map[current_entry] <= 1:
            output_collection.append(current_entry)
        idx += 1
    return output_collection