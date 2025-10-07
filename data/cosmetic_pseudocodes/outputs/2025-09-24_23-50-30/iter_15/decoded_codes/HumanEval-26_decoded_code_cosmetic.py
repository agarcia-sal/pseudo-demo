from collections import Counter
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    tally: Counter[T] = Counter(sequence)
    result_sequence: List[T] = [element for element in sequence if not (tally[element] > 1)]
    return result_sequence