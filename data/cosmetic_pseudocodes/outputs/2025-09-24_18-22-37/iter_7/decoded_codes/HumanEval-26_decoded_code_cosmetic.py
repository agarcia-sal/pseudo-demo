from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(input_sequence: Iterable[T]) -> List[T]:
    frequency_map = Counter(input_sequence)
    result_container: List[T] = []
    index = 0
    input_sequence_list = list(input_sequence)  # Ensure indexing

    while index < len(input_sequence_list):
        current_item = input_sequence_list[index]
        if frequency_map[current_item] <= 1:
            result_container.append(current_item)
        index += 1
    return result_container