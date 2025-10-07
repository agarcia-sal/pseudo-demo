from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map = Counter(sequence)
    filtered_result: List[T] = []
    index = 0
    while index < len(sequence):
        item = sequence[index]
        if frequency_map[item] <= 1:
            filtered_result.append(item)
        index += 1
    return filtered_result