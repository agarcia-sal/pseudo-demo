from collections import Counter
from typing import TypeVar, Sequence, List

T = TypeVar('T')


def remove_duplicates(sequence_input: Sequence[T]) -> List[T]:
    frequency_map = Counter(sequence_input)

    def filter_unique(index: int, accumulator: List[T]) -> List[T]:
        if index == len(sequence_input):
            return accumulator
        current_item = sequence_input[index]
        if frequency_map[current_item] <= 1:
            return filter_unique(index + 1, accumulator + [current_item])
        else:
            return filter_unique(index + 1, accumulator)

    return filter_unique(0, [])