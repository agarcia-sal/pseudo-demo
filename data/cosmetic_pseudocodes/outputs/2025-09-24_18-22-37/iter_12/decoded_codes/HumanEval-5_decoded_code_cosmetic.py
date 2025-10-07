from typing import Sequence, TypeVar, List

T = TypeVar('T')

def intersperse(sequence_A: Sequence[T], marker_B: T) -> List[T]:
    collection_C: List[T] = []

    if len(sequence_A) == 0:
        return collection_C

    index_D = 0
    limit_E = len(sequence_A) - 1

    while index_D < limit_E:
        item_F = sequence_A[index_D]
        collection_C.append(item_F)
        collection_C.append(marker_B)
        index_D += 1

    final_item_G = sequence_A[len(sequence_A) - 1]
    collection_C.append(final_item_G)

    return collection_C