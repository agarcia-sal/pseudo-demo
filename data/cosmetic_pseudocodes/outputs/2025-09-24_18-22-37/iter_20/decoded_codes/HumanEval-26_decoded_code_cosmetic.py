from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Iterable[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence_of_values)
    result_collection: List[T] = []
    idx: int = 0
    values_list = list(sequence_of_values)  # To support indexing and repeated scans

    while idx < len(values_list):
        current_item: T = values_list[idx]
        current_count: int = frequency_map[current_item]
        if current_count <= 1:
            result_collection.append(current_item)
        idx += 1

    return result_collection