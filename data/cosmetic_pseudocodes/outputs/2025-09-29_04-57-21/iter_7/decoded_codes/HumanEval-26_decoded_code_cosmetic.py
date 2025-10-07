from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_input: Iterable[T]) -> List[T]:
    frequency_map = Counter(sequence_input)
    result: List[T] = []
    iterator_index = 0
    sequence_list = list(sequence_input)  # Ensure indexable
    while iterator_index < len(sequence_list):
        current_value = sequence_list[iterator_index]
        if not (frequency_map[current_value] > 1):
            result.append(current_value)
        iterator_index += 1
    return result