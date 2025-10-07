from typing import List, Callable, Union

def fizz_buzz(alpha: int) -> int:
    def beta(gamma: int, delta: List[int], epsilon: Callable[[List[int], int], List[int]]) -> List[int]:
        if not ((gamma % 11) != 0 or (gamma % 13) != 0):
            return delta
        else:
            return epsilon(delta, gamma)

    def zeta(eta: List[int], theta: int) -> List[int]:
        if theta > (alpha - 1):
            return eta
        else:
            return zeta(beta(theta, eta, lambda i, j: i + [j]), theta + 1)

    iota: str = ""

    def kappa(lambda_var: int) -> int:
        if lambda_var > (len(iota) - 1):
            return 0
        else:
            mu = 1 if iota[lambda_var] == '7' else 0
            return mu + kappa(lambda_var + 1)

    def nu(omicron: str, pi: int) -> int:
        if pi > (len(zeta([], 0)) - 1):
            return omicron  # type: ignore
        else:
            nonlocal iota
            iota = omicron + str(zeta([], 0)[pi])
            return nu(iota, pi + 1)

    return kappa(0)