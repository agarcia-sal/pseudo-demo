from typing import List, Tuple


def is_nested(zeta: str) -> bool:
    def recurse_fill(alpha: List[int], beta: List[int], xi: int) -> Tuple[List[int], List[int]]:
        if xi == len(zeta):
            return alpha, beta
        if zeta[xi] == '[':
            return recurse_fill(alpha + [xi], beta, xi + 1)
        return recurse_fill(alpha, beta + [xi], xi + 1)

    def check_pairs(delta: List[int], epsilon: List[int], mu: int, nu: int) -> int:
        if mu == len(epsilon):
            return 0
        if delta[nu] < epsilon[mu]:
            return 1 + check_pairs(delta, epsilon, mu + 1, nu + 1)
        return check_pairs(delta, epsilon, mu + 1, nu)

    theta, iota = recurse_fill([], [], 0)
    kappa = len(iota) - 1

    def reversed_iota_helper(omega: int) -> List[int]:
        if omega < 0:
            return []
        return [iota[omega]] + reversed_iota_helper(omega - 1)

    def reversed_iota() -> List[int]:
        if kappa < 0:
            return []
        return [iota[kappa]] + reversed_iota_helper(kappa - 1)

    lambda_ = reversed_iota()
    sigma = check_pairs(theta, lambda_, 0, 0)
    return sigma >= 2