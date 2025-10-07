from collections import Counter
from typing import Sequence, TypeVar, List

T = TypeVar('T')

def remove_duplicates(input_sequence: Sequence[T]) -> List[T]:
    frequency_map = Counter(input_sequence)

    def iterator_function(position_index: int) -> List[T]:
        if position_index >= len(input_sequence):
            return []
        current_value = input_sequence[position_index]
        # Include current_value only if it occurs once in input_sequence
        return ([current_value] if frequency_map[current_value] <= 1 else []) + iterator_function(position_index + 1)

    return iterator_function(0)