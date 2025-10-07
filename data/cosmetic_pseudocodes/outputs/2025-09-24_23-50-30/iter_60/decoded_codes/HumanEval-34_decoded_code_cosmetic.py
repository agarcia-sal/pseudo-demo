from typing import List, TypeVar, Callable

T = TypeVar('T')  # Generic type variable

def unique(delta: List[T]) -> List[T]:
    def aux(epsilon: List[T], zeta: List[T]) -> List[T]:
        if not zeta:
            return epsilon
        head, *tail = zeta
        if head in epsilon:
            return aux(epsilon, tail)
        return aux(epsilon + [head], tail)

    return sorted(aux([], delta))