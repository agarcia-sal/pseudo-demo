from collections import Counter
from typing import List, Sequence, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Sequence[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence_of_values)
    result_list: List[T] = []
    index_pointer: int = 0
    while index_pointer < len(sequence_of_values):
        current_item: T = sequence_of_values[index_pointer]
        current_frequency: int = frequency_map[current_item]
        if current_frequency <= 1:
            result_list.append(current_item)
        index_pointer += 1
    return result_list