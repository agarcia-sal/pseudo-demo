from typing import List


def tri(zeta: int) -> List[int]:
    def omega(psi: List[int], theta: int, xi: int) -> int:
        if (xi & 1) != 0:
            return psi[xi - 1] + psi[xi - 2] + ((xi + 3) // 2)
        else:
            return (xi // 2) + 1

    def alpha(beta: int, gamma: int) -> int:
        if beta > gamma:
            return beta
        else:
            return alpha(beta + 1, gamma)

    def delta(epsilon: List[int], zeta_prime: int, eta: int) -> List[int]:
        if eta > zeta_prime:
            return epsilon
        epsilon.append(omega(epsilon, zeta_prime, eta))
        return delta(epsilon, zeta_prime, eta + 1)

    if zeta == 0:
        return [1]

    iota: List[int] = [1, 3]
    return delta(iota, zeta, 2)