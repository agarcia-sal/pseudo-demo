from typing import List, TypeVar

T = TypeVar('T')

def intersperse(a6: List[T], h2: T) -> List[T]:
    if not a6:
        return []
    r4: List[T] = []
    i7 = 1
    while i7 < len(a6):
        r4.append(a6[i7 - 1])
        r4.append(h2)
        i7 += 1
    r4.append(a6[-1])
    return r4