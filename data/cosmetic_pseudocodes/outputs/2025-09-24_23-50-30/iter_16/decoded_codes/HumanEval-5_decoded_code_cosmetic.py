from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], separator: T) -> List[T]:
    def insert_elements(src: Sequence[T], idx: int, acc: List[T]) -> List[T]:
        if idx >= len(src) - 1:
            return acc + [src[idx]]
        else:
            return insert_elements(src, idx + 1, acc + [src[idx], separator])

    if len(sequence) == 0:
        return []
    return insert_elements(sequence, 0, [])