from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], separator: T) -> List[T]:
    if not sequence:
        return []

    def build(idx: int, acc: List[T]) -> List[T]:
        if idx == len(sequence) - 1:
            return acc + [sequence[idx]]
        else:
            return build(idx + 1, acc + [sequence[idx], separator])

    return build(0, [])