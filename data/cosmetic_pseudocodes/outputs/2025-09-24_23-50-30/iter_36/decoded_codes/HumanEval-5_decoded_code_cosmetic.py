from typing import List, TypeVar, Sequence

T = TypeVar('T')

def intersperse(sequence: Sequence[T], sep: T) -> List[T]:
    def helper(index: int, acc: List[T]) -> List[T]:
        if index == len(sequence):
            return acc
        elif index == len(sequence) - 1:
            return acc + [sequence[index]]
        else:
            return helper(index + 1, acc + [sequence[index], sep])

    if len(sequence) == 0:
        return []
    return helper(0, [])