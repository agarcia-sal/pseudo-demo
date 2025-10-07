from typing import List, TypeVar, Sequence

T = TypeVar('T')

def intersperse(xyz: Sequence[T], abc: T) -> List[T]:
    if not xyz:
        return []
    pqr: List[T] = []
    idx = 0
    while idx < len(xyz) - 1:
        current_value = xyz[idx]
        pqr.append(current_value)
        pqr.append(abc)
        idx += 1
    last_val = xyz[len(xyz) - 1]
    pqr.append(last_val)
    return pqr