from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(enumerable: Sequence[T]) -> T:
    accumulator: T = enumerable[0]
    index_cursor: int = 1
    while index_cursor < len(enumerable):
        if not (enumerable[index_cursor] <= accumulator):
            accumulator = enumerable[index_cursor]
        index_cursor += 1
    return accumulator