from typing import Iterable, TypeVar, List
from collections import Counter

T = TypeVar('T')

def remove_duplicates(sequence: Iterable[T]) -> List[T]:
    frequency_map = Counter(sequence)
    result = [element for element in sequence if frequency_map[element] <= 1]
    return result