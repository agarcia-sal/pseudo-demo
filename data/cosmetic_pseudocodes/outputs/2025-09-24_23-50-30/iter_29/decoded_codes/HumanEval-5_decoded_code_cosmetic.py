from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], sep: T) -> List[T]:
    if not sequence:
        return []

    def intersperse_tail(index: int, acc: List[T]) -> List[T]:
        if index == len(sequence) - 1:
            return acc + [sequence[index]]
        else:
            return intersperse_tail(index + 1, acc + [sequence[index], sep])

    return intersperse_tail(0, [])