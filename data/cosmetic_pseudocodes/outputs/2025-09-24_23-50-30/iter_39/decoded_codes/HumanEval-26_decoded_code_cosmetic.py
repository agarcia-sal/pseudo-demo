from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence_parameter: Sequence[T]) -> List[T]:
    auxiliary_count_map = Counter(sequence_parameter)
    result_collection: List[T] = []
    position_marker = 0

    while position_marker < len(sequence_parameter):
        current_item = sequence_parameter[position_marker]
        if auxiliary_count_map[current_item] <= 1:
            result_collection.append(current_item)
        position_marker += 1

    return result_collection