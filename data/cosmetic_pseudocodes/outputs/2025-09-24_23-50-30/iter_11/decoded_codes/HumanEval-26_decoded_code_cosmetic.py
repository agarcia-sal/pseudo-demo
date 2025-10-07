from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    counts_map = Counter(sequence)
    filtered: List[T] = [element for element in sequence if counts_map[element] == 1]
    return filtered