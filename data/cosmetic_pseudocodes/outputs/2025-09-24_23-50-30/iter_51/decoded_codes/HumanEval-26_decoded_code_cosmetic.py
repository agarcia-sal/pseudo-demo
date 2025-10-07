from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_values: List[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence_values)
    filtered_collection: List[T] = []

    def recursive_filter(index: int) -> None:
        if index >= len(sequence_values):
            return
        current_value = sequence_values[index]
        if not (frequency_map[current_value] > 1):
            filtered_collection.append(current_value)
        recursive_filter(index + 1)

    recursive_filter(0)
    return filtered_collection