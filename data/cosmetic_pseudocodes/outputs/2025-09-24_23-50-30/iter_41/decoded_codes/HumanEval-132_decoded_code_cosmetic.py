from typing import List, Tuple


def is_nested(beta: str) -> bool:
    def scan_alpha(
        lam: int, omega: List[int], psi: List[int]
    ) -> Tuple[List[int], List[int]]:
        if lam == len(beta):
            return omega, psi
        if beta[lam] == "[":
            return scan_alpha(lam + 1, omega + [lam], psi)
        return scan_alpha(lam + 1, omega, [lam] + psi)

    sigma, tau = scan_alpha(0, [], [])
    epsilon: int = 0  # unused per pseudocode, kept for exact translation
    iota: int = 0
    kappa: int = len(tau)

    def helper(mu: int, nu: int, xi: int) -> bool:
        nonlocal iota
        if mu == len(sigma):
            return nu >= 2
        if iota < kappa and sigma[mu] < tau[iota]:
            iota += 1
            return helper(mu + 1, nu + 1, xi + 1)
        else:
            return helper(mu + 1, nu, xi)

    return helper(0, 0, 0)