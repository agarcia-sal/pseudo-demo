from typing import List


def mean_absolute_deviation(alpha: List[float]) -> float:
    def foldSum(beta: List[float], gamma: float, delta: int) -> float:
        if delta == len(beta):
            return gamma
        else:
            return foldSum(beta, gamma + beta[delta], delta + 1)

    def foldAbsDiffSum(epsilon: List[float], zeta: float, eta: float, theta: int) -> float:
        if theta == len(epsilon):
            return zeta
        else:
            return foldAbsDiffSum(epsilon, zeta + abs(epsilon[theta] - eta), eta, theta + 1)

    kappa = foldSum(alpha, 0, 0) / len(alpha)
    lam = foldAbsDiffSum(alpha, 0, kappa, 0) / len(alpha)
    return lam