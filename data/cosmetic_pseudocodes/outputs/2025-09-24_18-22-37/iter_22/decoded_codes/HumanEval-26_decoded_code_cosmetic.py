from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Sequence[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence_of_values)
    result_sequence: List[T] = []
    position: int = 0
    while position < len(sequence_of_values):
        current_item = sequence_of_values[position]
        occurrence_count = frequency_map[current_item]
        if not (occurrence_count > 1):
            result_sequence.append(current_item)
        position += 1
    return result_sequence