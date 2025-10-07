from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], glue: T) -> List[T]:
    if not sequence:
        return []

    def helper(idx: int, acc: List[T]) -> List[T]:
        if idx == len(sequence) - 1:
            return acc + [sequence[idx]]
        return helper(idx + 1, acc + [sequence[idx], glue])

    return helper(0, [])