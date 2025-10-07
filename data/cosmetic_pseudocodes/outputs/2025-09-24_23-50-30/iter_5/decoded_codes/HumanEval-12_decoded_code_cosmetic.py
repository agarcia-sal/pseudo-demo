from typing import Collection, Optional, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def longest(collection: Collection[T]) -> Optional[T]:
    if not collection:
        return None

    lim = 0
    for element in collection:
        length = len(element)
        if lim < length:
            lim = length

    index = 0
    collection_seq = list(collection)  # To allow index access if collection is not a sequence
    while index < len(collection_seq):
        if len(collection_seq[index]) == lim:
            return collection_seq[index]
        index += 1
    return None