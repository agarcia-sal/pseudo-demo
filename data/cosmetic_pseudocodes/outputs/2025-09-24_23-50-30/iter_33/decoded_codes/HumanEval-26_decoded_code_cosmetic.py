from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence)
    result_list: List[T] = [each_item for each_item in sequence if frequency_map[each_item] <= 1]
    return result_list