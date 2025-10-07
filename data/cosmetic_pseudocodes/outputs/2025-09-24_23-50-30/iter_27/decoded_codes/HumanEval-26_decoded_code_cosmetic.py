from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Iterable[T]) -> List[T]:
    frequency_map = Counter(sequence_of_values)
    filtered_values: List[T] = []
    index_tracker = 0
    sequence_list = list(sequence_of_values)  # To support indexing and length
    while index_tracker < len(sequence_list):
        candidate = sequence_list[index_tracker]
        if frequency_map[candidate] <= 1:
            filtered_values.append(candidate)
        index_tracker += 1
    return filtered_values