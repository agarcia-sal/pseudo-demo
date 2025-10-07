from typing import List, TypeVar

T = TypeVar('T')

def intersperse(alpha: List[T], beta: T) -> List[T]:
    def insertions(arr: List[T], idx: int, acc: List[T]) -> List[T]:
        if idx == len(arr):
            return acc
        return insertions(arr, idx + 1, acc + [arr[idx], beta])

    if not alpha:
        return []
    partial = insertions(alpha, 0, [])
    # partial ends with an extra beta, remove the last beta and add the last element of alpha
    return partial[:len(partial) - 1] + [alpha[-1]]