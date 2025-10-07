from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(collection_of_values: Iterable[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(collection_of_values)
    results: List[T] = []
    cursor: int = 0
    values_list = list(collection_of_values)  # to support indexing
    while cursor < len(values_list):
        candidate = values_list[cursor]
        if frequency_map[candidate] <= 1:
            results.append(candidate)
        cursor += 1
    return results