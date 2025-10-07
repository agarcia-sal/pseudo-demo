from typing import TypeVar, Iterable, List

T = TypeVar('T')

def unique(x: Iterable[T]) -> List[T]:
    seen = set()
    result: List[T] = []
    for item in x:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result