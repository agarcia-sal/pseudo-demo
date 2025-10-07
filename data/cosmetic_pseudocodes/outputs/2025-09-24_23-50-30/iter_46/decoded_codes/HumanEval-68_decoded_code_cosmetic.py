from typing import List, Optional

def pluck(delta: List[int]) -> List[int]:
    def epsilon(beta: int, gamma: int) -> List[int]:
        if beta >= gamma:
            return []
        return [gamma] if (gamma % 2) == 0 else []

    def zeta(eta: List[int], theta: List[int], i: int) -> List[int]:
        if i >= len(eta):
            return theta
        if (eta[i] % 2) != 0:
            return zeta(eta, theta, i + 1)
        return zeta(eta, theta + [eta[i]], i + 1)

    def iota(kappa: List[int]) -> List[int]:
        return kappa

    def lambda_(mu: List[int]) -> List[int]:
        if len(mu) == 0:
            return []
        xi = mu[0]
        omicron = 0
        pi = 1
        while pi < len(mu):
            if mu[pi] < xi:
                xi = mu[pi]
                omicron = pi
            pi += 1
        return [xi, omicron]

    tau = zeta(delta, [], 0)
    if not (len(delta) > 0):
        return []
    if len(tau) == 0:
        return []
    return lambda_(tau)