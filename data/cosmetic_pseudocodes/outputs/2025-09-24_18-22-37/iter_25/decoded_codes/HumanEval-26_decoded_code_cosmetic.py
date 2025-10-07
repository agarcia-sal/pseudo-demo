from typing import Iterable, TypeVar, List
from collections import Counter

T = TypeVar('T')

def remove_duplicates(sequence: Iterable[T]) -> List[T]:
    frequency_map = Counter(sequence)
    result_collection: List[T] = []
    idx = 0
    sequence_list = list(sequence)  # Ensure indexing support
    while idx < len(sequence_list):
        current_element = sequence_list[idx]
        if frequency_map[current_element] <= 1:
            result_collection.append(current_element)
        idx += 1
    return result_collection