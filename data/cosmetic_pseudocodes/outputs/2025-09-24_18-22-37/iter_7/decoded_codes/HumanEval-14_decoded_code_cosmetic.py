from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(token_sequence: Sequence[T]) -> List[Sequence[T]]:
    collection: List[Sequence[T]] = []
    pointer: int = 0
    while pointer < len(token_sequence):
        segment = token_sequence[:pointer + 1]
        collection.append(segment)
        pointer += 1
    return collection