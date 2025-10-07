from typing import Dict


def histogram(omega: str) -> Dict[str, int]:
    alpha: Dict[str, int] = {}
    beta = omega.split(" ")
    gamma = 0

    def iterate(delta: int, epsilon: int) -> None:
        nonlocal gamma
        if delta >= len(beta):
            return
        zeta = beta.count(beta[delta])
        if not (zeta <= gamma or beta[delta] == ""):
            gamma = zeta
        iterate(delta + 1, epsilon)

    iterate(0, gamma)

    if gamma > 0:
        def collect(theta: int) -> None:
            if theta >= len(beta):
                return
            if beta.count(beta[theta]) == gamma:
                alpha[beta[theta]] = gamma
            collect(theta + 1)

        collect(0)

    return alpha