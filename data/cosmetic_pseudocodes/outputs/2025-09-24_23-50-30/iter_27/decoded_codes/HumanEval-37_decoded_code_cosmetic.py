from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_even(collection_parameter: Sequence[T]) -> List[T]:
    beta: List[T] = []
    omega: List[T] = []
    i = 0
    while i < len(collection_parameter):
        if i % 2 == 0:
            beta.append(collection_parameter[i])
        else:
            omega.append(collection_parameter[i])
        i += 1

    gamma = 0
    while gamma < len(beta) - 1:
        delta = gamma + 1
        while delta < len(beta):
            if not (beta[gamma] <= beta[delta]):
                beta[gamma], beta[delta] = beta[delta], beta[gamma]
            delta += 1
        gamma += 1

    epsilon: List[T] = []
    zeta = 0
    while zeta < len(omega):
        epsilon.append(beta[zeta])
        epsilon.append(omega[zeta])
        zeta += 1

    if len(beta) > len(omega):
        epsilon.append(beta[-1])

    return epsilon