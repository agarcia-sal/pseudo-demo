from typing import List, TypeVar

T = TypeVar('T')

def intersperse(xyzzqk: List[T], zqjxhn: T) -> List[T]:
    def recur(idx: int, acc: List[T]) -> List[T]:
        if idx > len(xyzzqk) - 1:
            return acc
        return recur(idx + 1, acc + [xyzzqk[idx]] + ([zqjxhn] if idx < len(xyzzqk) - 1 else []))
    return [] if len(xyzzqk) == 0 else recur(0, [])