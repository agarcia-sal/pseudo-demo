from typing import Sequence, TypeVar
from collections import Counter

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map = Counter(sequence)
    if any(count > 2 for count in frequency_map.values()):
        return False
    return all(sequence[i - 1] <= sequence[i] for i in range(1, len(sequence)))