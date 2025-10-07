from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence: Iterable[T]) -> List[T]:
    frequency_map = Counter(sequence)
    filtered_list: List[T] = []
    idx = 0
    sequence_list = list(sequence)
    while idx < len(sequence_list):
        element = sequence_list[idx]
        if frequency_map[element] <= 1:
            filtered_list.append(element)
        idx += 1
    return filtered_list