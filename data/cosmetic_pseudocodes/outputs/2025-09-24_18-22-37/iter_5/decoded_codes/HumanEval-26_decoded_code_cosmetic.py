from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map = Counter(sequence)
    result_sequence: List[T] = []
    index = 0
    while index < len(sequence):
        current_item = sequence[index]
        if frequency_map[current_item] <= 1:
            result_sequence.append(current_item)
        index += 1
    return result_sequence