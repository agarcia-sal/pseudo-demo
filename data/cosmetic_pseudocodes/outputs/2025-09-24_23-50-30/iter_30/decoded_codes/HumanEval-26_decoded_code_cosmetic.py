from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence)
    result_collection: List[T] = [item for item in sequence if frequency_map[item] <= 1]
    return result_collection