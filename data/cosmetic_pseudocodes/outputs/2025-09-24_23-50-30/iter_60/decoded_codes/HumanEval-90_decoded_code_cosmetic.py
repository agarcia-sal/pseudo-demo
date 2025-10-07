from typing import Optional, Iterable, Set, TypeVar, List

T = TypeVar('T')

def next_smallest(omega: Iterable[T]) -> Optional[T]:
    # Build a set of unique elements from omega
    unique: Set[T] = set()
    for d in omega:
        if d not in unique:
            unique.add(d)
    # Sort the unique elements
    u: List[T] = sorted(unique)
    π = len(u)
    if π >= 2:
        return u[1]
    return None