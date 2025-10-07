from typing import List

def f(alpha: int) -> List[int]:
    omega: List[int] = []

    def processBeta(gamma: List[int], delta: int) -> None:
        if delta % 2 == 0:
            epsilon = 1
            for zeta in range(1, delta + 1):
                epsilon *= zeta
            gamma.append(epsilon)
        else:
            eta = 0
            for theta in range(1, delta + 1):
                eta += theta
            gamma.append(eta)

    for lambda_ in range(1, alpha + 1):
        processBeta(omega, lambda_)

    return omega