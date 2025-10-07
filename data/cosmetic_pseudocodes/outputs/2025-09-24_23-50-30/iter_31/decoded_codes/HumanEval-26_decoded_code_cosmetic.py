from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence: Iterable[T]) -> List[T]:
    tracker: Counter[T] = Counter(sequence)
    output_collection: List[T] = []
    for datum in sequence:
        if tracker[datum] <= 1:
            output_collection.append(datum)
    return output_collection