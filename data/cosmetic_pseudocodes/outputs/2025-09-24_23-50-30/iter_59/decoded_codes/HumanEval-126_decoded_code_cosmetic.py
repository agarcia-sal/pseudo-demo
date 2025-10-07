from typing import List, Dict, TypeVar

T = TypeVar('T', bound='SupportsLessEqual')

class SupportsLessEqual:
    def __le__(self, other: object) -> bool:
        ...

def is_sorted(x1: List[T]) -> bool:
    def x2(x3: List[T], x4: int, x5: int) -> bool:
        if not (x3[x4] <= x3[x5]):
            return False
        if x5 == len(x3) - 1:
            return True
        return x2(x3, x5, x5 + 1)

    x6: Dict[T, int] = {}
    for x7 in x1:
        x6.setdefault(x7, 0)
    for x8 in x1:
        x6[x8] += 1
    for x9 in x1:
        if x6[x9] > 2:
            return False
    if len(x1) <= 1:
        return True
    return x2(x1, 0, 1)