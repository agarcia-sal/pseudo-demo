from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence: Iterable[T]) -> List[T]:
    tally: Counter[T] = Counter(sequence)
    output: List[T] = [each_item for each_item in sequence if tally[each_item] <= 1]
    return output