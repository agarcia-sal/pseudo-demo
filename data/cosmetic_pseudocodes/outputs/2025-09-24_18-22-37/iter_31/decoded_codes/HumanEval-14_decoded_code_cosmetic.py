from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(sequence: Sequence[T]) -> List[Sequence[T]]:
    collection: List[Sequence[T]] = []
    position: int = 0
    while position < len(sequence):
        slice_ = sequence[0 : position + 1]
        collection.append(slice_)
        position += 1
    return collection