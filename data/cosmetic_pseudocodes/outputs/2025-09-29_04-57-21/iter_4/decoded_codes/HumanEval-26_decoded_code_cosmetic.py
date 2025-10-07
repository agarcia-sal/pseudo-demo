from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence)
    unique_elements: List[T] = []
    position: int = 0
    while position < len(sequence):
        current_item: T = sequence[position]
        if frequency_map[current_item] <= 1:
            unique_elements.append(current_item)
        position += 1
    return unique_elements