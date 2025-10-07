from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(collection_of_values: Iterable[T]) -> List[T]:
    histogram: Counter[T] = Counter(collection_of_values)
    unique_items: List[T] = [item for item in collection_of_values if histogram[item] <= 1]
    return unique_items