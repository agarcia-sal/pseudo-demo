from typing import List

def f(beta: int) -> List[int]:
    alpha: List[int] = []
    delta: int = 1
    lambd: int = 1  # 'lambda' is a keyword in Python

    def zeta(epsilon: int, omega: int, psi: int) -> int:
        if psi > omega:
            return epsilon
        else:
            return zeta(epsilon * psi, omega, psi + 1)

    def theta(kappa: int, mu: int, nu: int) -> int:
        if nu > mu:
            return kappa
        else:
            return theta(kappa + nu, mu, nu + 1)

    def rho(xi: int) -> int:
        if xi % 2 == 0:
            return zeta(1, xi, 1)
        else:
            return theta(0, xi, 1)

    def sigma(tau: int) -> None:
        if tau > beta:
            return
        else:
            upsilon: int = rho(tau)
            alpha.append(upsilon)
            sigma(tau + 1)

    sigma(1)
    return alpha