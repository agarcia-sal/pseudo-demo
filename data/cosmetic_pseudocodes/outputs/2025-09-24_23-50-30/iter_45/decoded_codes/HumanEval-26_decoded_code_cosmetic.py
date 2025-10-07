from collections import Counter
from typing import List, Sequence, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence)
    filtered_result: List[T] = [item for item in sequence if frequency_map[item] <= 1]
    return filtered_result