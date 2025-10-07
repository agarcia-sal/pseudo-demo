from typing import TypeVar, List, Sequence

T = TypeVar('T')

def intersperse(container: Sequence[T], separator: T) -> List[T]:
    def buildup(index: int, collected: List[T]) -> List[T]:
        if index >= len(container) - 1:
            return collected + [container[index]]
        return buildup(index + 1, collected + [container[index], separator])

    if len(container) == 0:
        return []
    return buildup(0, [])