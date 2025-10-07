from typing import List

def f(beta: int) -> List[int]:
    alpha: List[int] = []

    def walk(zeta: int, eta: int, xi: int, rho: int) -> None:
        if zeta > beta:
            return
        if zeta % 2 == 0:
            psi = 1

            def accumulate(tau: int, upsilon: int) -> None:
                nonlocal psi
                if tau > zeta:
                    return
                psi *= tau
                accumulate(tau + 1, upsilon)

            accumulate(1, 0)
            alpha.append(psi)
        else:
            phi = 0

            def accumulate_sigma(lambda_: int, mu: int) -> None:
                nonlocal phi
                if lambda_ > zeta:
                    return
                phi += lambda_
                accumulate_sigma(lambda_ + 1, mu)

            accumulate_sigma(1, 0)
            alpha.append(phi)
        walk(zeta + 1, eta, xi, rho)

    walk(1, 0, 0, 0)
    return alpha