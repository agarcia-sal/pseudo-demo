from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(values: List[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(values)
    result: List[T] = [item for item in values if frequency_map[item] <= 1]
    return result