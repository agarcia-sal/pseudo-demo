from typing import List, TypeVar

T = TypeVar('T')

def common(alpha: List[T], beta: List[T]) -> List[T]:
    gamma: List[T] = []
    for delta in alpha:
        if delta in beta and delta not in gamma:
            gamma.append(delta)
    epsilon: List[T] = gamma
    epsilon.sort()
    return epsilon