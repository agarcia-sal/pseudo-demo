from typing import Iterable, Optional, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def longest(collection: Iterable[T]) -> Optional[T]:
    collection_seq = list(collection)  # Convert to sequence for indexing and length
    if not collection_seq:
        return None

    max_len = float('-inf')
    for q in collection_seq:
        q_len = len(q)
        if q_len > max_len:
            max_len = q_len

    for r in range(len(collection_seq)):
        if len(collection_seq[r]) == max_len:
            return collection_seq[r]