from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)  # assuming values comparable to 0 (numbers)

def get_positive(sequence_of_values: Iterable[T]) -> List[T]:
    collection_of_positives: List[T] = []
    for candidate in sequence_of_values:
        if not (candidate <= 0):
            collection_of_positives.append(candidate)
    return collection_of_positives