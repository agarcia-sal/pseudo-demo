from typing import Sequence, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(collection_a: Sequence[T], collection_b: Sequence[T]) -> Sequence[T]:
    accumulator_a: int = 0
    index_a: int = 0
    while index_a < len(collection_a):
        item_a = collection_a[index_a]
        accumulator_a += len(item_a)
        index_a += 1
    accumulator_b: int = 0
    index_b: int = 0
    while index_b < len(collection_b):
        item_b = collection_b[index_b]
        accumulator_b += len(item_b)
        index_b += 1
    if not (accumulator_a > accumulator_b):
        return collection_a
    return collection_b