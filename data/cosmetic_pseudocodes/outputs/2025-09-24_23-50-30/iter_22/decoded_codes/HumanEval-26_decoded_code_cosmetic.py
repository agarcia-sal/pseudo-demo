from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(input_sequence: Iterable[T]) -> List[T]:
    tally: Counter[T] = Counter(input_sequence)
    output_sequence: List[T] = [item for item in input_sequence if tally[item] <= 1]
    return output_sequence