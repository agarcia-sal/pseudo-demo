from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map = Counter(sequence)
    filtered_elements: List[T] = []
    for index in range(len(sequence)):
        current_value = sequence[index]
        if frequency_map[current_value] <= 1:
            filtered_elements.append(current_value)
    return filtered_elements