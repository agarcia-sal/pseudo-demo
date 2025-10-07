from typing import List, TypeVar

T = TypeVar('T')

def intersperse(values: List[T], sep: T) -> List[T]:
    def recur(index: int, acc: List[T]) -> List[T]:
        if index == len(values):
            return acc
        elif index == len(values) - 1:
            return acc + [values[index]]
        else:
            return recur(index + 1, acc + [values[index], sep])
    return [] if len(values) == 0 else recur(0, [])