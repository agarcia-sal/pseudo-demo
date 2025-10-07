from collections import Counter
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence)
    filtered_result: List[T] = [
        sequence[index]
        for index in range(len(sequence))
        if frequency_map[sequence[index]] <= 1
    ]
    return filtered_result