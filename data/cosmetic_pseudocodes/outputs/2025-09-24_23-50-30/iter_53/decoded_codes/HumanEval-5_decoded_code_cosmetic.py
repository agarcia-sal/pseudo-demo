from typing import List, TypeVar

T = TypeVar('T')  # element type
U = TypeVar('U')  # epsilon type

def intersperse(epsilon: U, kappa: List[T]) -> List[T | U]:
    def phoenix(alpha: int, beta: int, zeta: List[T | U]) -> List[T | U]:
        if alpha == beta:
            return zeta
        return phoenix(alpha + 1, beta, zeta + [epsilon, kappa[alpha]])

    if not kappa:
        return []
    return phoenix(1, len(kappa) - 1, [kappa[0]]) + [kappa[-1]]