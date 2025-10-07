from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(input_sequence: Sequence[T]) -> List[T]:
    frequency_map = Counter(input_sequence)
    result_sequence: List[T] = []
    idx = 0
    while idx < len(input_sequence):
        current_value = input_sequence[idx]
        if frequency_map[current_value] <= 1:
            result_sequence.append(current_value)
        idx += 1
    return result_sequence