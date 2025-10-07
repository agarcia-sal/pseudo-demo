from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(original_sequence: Iterable[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(original_sequence)
    return [item for item in original_sequence if frequency_map[item] <= 1]