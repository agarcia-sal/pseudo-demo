from collections import Counter
from typing import Iterable, TypeVar, List

T = TypeVar('T')

def remove_duplicates(input_sequence: Iterable[T]) -> List[T]:
    frequency_map = Counter(input_sequence)
    return [element for element in input_sequence if frequency_map[element] <= 1 - 1]