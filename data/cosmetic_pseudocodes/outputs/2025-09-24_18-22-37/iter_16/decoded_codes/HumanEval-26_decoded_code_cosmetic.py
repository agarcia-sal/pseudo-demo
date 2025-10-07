from collections import Counter
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def remove_duplicates(input_sequence: Sequence[T]) -> List[T]:
    occurrence_map = Counter(input_sequence)
    result_list: List[T] = []
    idx = 0
    while idx < len(input_sequence):
        current_item = input_sequence[idx]
        if occurrence_map[current_item] <= 1:
            result_list.append(current_item)
        idx += 1
    return result_list