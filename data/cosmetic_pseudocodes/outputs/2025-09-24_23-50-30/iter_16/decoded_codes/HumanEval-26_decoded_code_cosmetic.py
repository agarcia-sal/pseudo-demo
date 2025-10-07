from collections import Counter
from functools import reduce
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(input_sequence: Iterable[T]) -> List[T]:
    tally_map = Counter(input_sequence)

    def gather_unique(accumulator: List[T], current_item: T) -> List[T]:
        return accumulator + [current_item] if tally_map[current_item] <= 1 else accumulator

    return reduce(gather_unique, input_sequence, [])