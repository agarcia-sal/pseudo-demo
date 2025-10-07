from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(input_sequence: Iterable[T]) -> List[T]:
    tally_map = Counter(input_sequence)
    def filter_predicate(x: T) -> bool:
        return not (tally_map[x] > 1)
    filtered_list: List[T] = [item for item in input_sequence if filter_predicate(item)]
    return filtered_list