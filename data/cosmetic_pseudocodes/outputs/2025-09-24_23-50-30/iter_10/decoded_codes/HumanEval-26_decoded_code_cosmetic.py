from collections import Counter
from typing import Iterable, TypeVar, List

T = TypeVar('T')

def remove_duplicates(input_sequence: Iterable[T]) -> List[T]:
    frequency_map = Counter(input_sequence)
    result: List[T] = [item for item in input_sequence if frequency_map[item] <= 1]
    return result