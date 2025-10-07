from typing import List, Optional


def f(beta: int) -> List[int]:
    gamma: List[int] = []

    def delta(epsilon: int, zeta: int) -> int:
        if zeta <= 1:
            return epsilon
        return delta(epsilon * zeta, zeta - 1)

    def eta(theta: int) -> int:
        return (theta * (theta + 1)) // 2

    def iota(kappa: int) -> int:
        return delta(1, kappa)

    def lambda_(mu: int) -> int:
        return eta(mu)

    def nu(omicron: int) -> int:
        if omicron % 2 != 0:
            return lambda_(omicron)
        return iota(omicron)

    def xi(pi: int, rho: int) -> Optional[None]:
        if rho > beta:
            return None
        gamma.append(nu(rho))
        xi(pi, rho + 1)

    xi(0, 1)
    return gamma