from typing import List, TypeVar

T = TypeVar('T')

def unique(sequence: List[T]) -> List[T]:
    def helper(index: int, acc: List[T]) -> List[T]:
        if index == len(sequence):
            return acc
        if sequence[index] in acc:
            return helper(index + 1, acc)
        return helper(index + 1, acc + [sequence[index]])
    return sorted(helper(0, []))