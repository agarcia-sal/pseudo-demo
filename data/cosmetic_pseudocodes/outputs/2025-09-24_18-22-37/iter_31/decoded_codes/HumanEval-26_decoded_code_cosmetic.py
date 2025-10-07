from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Iterable[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence_of_values)
    result_list: List[T] = [value for value in sequence_of_values if frequency_map[value] <= 1]
    return result_list