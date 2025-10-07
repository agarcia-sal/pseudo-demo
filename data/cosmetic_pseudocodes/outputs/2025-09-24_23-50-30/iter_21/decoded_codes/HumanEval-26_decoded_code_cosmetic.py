from collections import Counter
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def remove_duplicates(numbers_sequence: Sequence[T]) -> List[T]:
    frequency_map = Counter(numbers_sequence)
    return [item for item in numbers_sequence if frequency_map[item] <= 1]