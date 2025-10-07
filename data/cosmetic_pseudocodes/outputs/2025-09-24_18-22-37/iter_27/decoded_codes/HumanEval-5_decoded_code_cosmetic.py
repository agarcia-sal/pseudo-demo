from typing import List, TypeVar

T = TypeVar('T')

def intersperse(sigma: List[T], omega: T) -> List[T]:
    delta: List[T] = []

    if sigma:
        psi: int = 0

        while psi < len(sigma) - 1:
            zeta: T = sigma[psi]
            delta.append(zeta)
            delta.append(omega)
            psi += 1

        theta: T = sigma[len(sigma) - 1]
        delta.append(theta)

        return delta
    else:
        return []