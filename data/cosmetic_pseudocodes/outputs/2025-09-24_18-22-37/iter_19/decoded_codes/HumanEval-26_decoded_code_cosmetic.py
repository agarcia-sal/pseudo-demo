from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(numbers_collection: Iterable[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(numbers_collection)
    unique_items: List[T] = []
    idx = 0
    numbers_list = list(numbers_collection)  # Allow indexing via idx
    while idx < len(numbers_list):
        current_element = numbers_list[idx]
        if not (frequency_map[current_element] > 1):
            unique_items.append(current_element)
        idx += 1
    return unique_items