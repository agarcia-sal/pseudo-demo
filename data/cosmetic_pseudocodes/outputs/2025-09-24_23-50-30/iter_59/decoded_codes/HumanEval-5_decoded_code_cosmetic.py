from typing import List, TypeVar

T = TypeVar('T')

def intersperse(p: List[T], q: T) -> List[T]:
    if not p:
        return []

    r: List[T] = []

    def aux(a: List[T], b: List[T]) -> List[T]:
        if not a:
            return b
        c, d = a[0], a[1:]
        return aux(d, b + [c, q])

    s = aux(p[:-1], r)
    return s + [p[-1]]