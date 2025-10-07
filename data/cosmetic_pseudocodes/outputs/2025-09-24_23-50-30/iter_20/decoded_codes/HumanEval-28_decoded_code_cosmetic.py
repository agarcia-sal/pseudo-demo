from typing import Iterable, Sequence, TypeVar

T = TypeVar('T')

def concatenate(source_collection: Iterable[Sequence[T]]) -> Sequence[T]:
    accumulator: Sequence[T] = []
    for element in source_collection:
        accumulator = accumulator + element
    return accumulator