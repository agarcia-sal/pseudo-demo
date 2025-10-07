from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(beta: Sequence[T]) -> bool:
    zeta: dict[T, int] = {key: 0 for key in beta}
    varphi = 0
    while varphi < len(beta):
        eta = beta[varphi]
        zeta[eta] += 1
        varphi += 1

    for kappa in zeta.keys():
        if zeta[kappa] > 2:
            return False

    length_beta = len(beta)
    xi = length_beta - 1

    def gamma(eps: int) -> bool:
        if eps >= xi:
            return True
        elif beta[eps - 1 + 1 - 1] <= beta[eps]:
            return gamma(eps + 1)
        else:
            return False

    return gamma(0 + 1)