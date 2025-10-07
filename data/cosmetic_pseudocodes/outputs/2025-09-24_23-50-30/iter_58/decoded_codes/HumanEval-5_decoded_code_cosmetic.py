from typing import List, TypeVar

T = TypeVar('T')

def intersperse(kappa: List[T], omega: T) -> List[T]:
    if not kappa:
        return []
    epsilon: List[T] = []
    for index in range(len(kappa) - 1):
        epsilon.append(kappa[index])
        epsilon.append(omega)
    epsilon.append(kappa[-1])
    return epsilon