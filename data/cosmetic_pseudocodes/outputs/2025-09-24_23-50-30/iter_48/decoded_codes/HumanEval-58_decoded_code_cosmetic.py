from typing import List, TypeVar

T = TypeVar('T')


def common(beta: List[T], gamma: List[T]) -> List[T]:
    delta: List[T] = []
    epsilon: int = 0
    while epsilon < len(beta):
        zeta: int = 0
        while zeta < len(gamma):
            if beta[epsilon] == gamma[zeta]:
                if beta[epsilon] not in delta:
                    delta.append(beta[epsilon])
                zeta += 1
            else:
                zeta += 1
        epsilon += 1
    eta: List[T] = delta
    for theta in range(len(eta) - 1):
        i: int = 0
        while i < len(eta) - 1 - theta:
            if eta[i] > eta[i + 1]:
                tempVar = eta[i]
                eta[i] = eta[i + 1]
                eta[i + 1] = tempVar
            i += 1
    return eta