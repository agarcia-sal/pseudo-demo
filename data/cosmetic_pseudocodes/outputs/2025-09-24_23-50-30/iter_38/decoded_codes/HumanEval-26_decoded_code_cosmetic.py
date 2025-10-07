from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar("T")

def remove_duplicates(sequence_of_values: Iterable[T]) -> List[T]:
    frequency_map = Counter(sequence_of_values)
    return [item for item in sequence_of_values if frequency_map[item] <= 1]