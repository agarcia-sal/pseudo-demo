from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequencies = Counter(sequence)
    return [elem for elem in sequence if frequencies[elem] <= 1]