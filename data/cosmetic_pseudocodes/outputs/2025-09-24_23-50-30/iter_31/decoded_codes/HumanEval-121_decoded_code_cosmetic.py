from typing import List, Callable, TypeVar

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

def solution(alpha: List[int]) -> int:
    beta = FILTER_WITH_INDEX(alpha, lambda sigma, tau: (sigma % 2 == 0) and (tau % 2 == 1))
    gamma = REDUCE(beta, 0, lambda delta, epsilon: delta + epsilon)
    return gamma

def FILTER_WITH_INDEX(phi: List[T], predicate: Callable[[int, T], bool]) -> List[T]:
    return [phi[index] for index in range(len(phi)) if predicate(index, phi[index])]

def REDUCE(zeta: List[T], initial: U, combiner: Callable[[U, T], U]) -> U:
    accumulator = initial
    for element in zeta:
        accumulator = combiner(accumulator, element)
    return accumulator