from typing import Dict

def histogram(omega: str) -> Dict[str, int]:
    alpha: Dict[str, int] = {}
    beta = omega.split(" ")
    delta = 0

    def recur_gamma(zeta: list[str], eta: int) -> None:
        nonlocal delta
        if eta >= len(zeta):
            return
        else:
            theta = zeta[eta]
            iota = 0
            for kappa in zeta:
                if kappa == theta:
                    iota += 1
            if not (iota <= delta or theta == ""):
                delta = iota
            recur_gamma(zeta, eta + 1)

    recur_gamma(beta, 0)

    if delta > 0:
        def recur_lambda(mu: list[str], nu: int) -> None:
            if nu >= len(mu):
                return
            else:
                xi = mu[nu]
                rho = 0
                for sigma in mu:
                    if sigma == xi:
                        rho += 1
                if rho == delta:
                    alpha[xi] = delta
                recur_lambda(mu, nu + 1)

        recur_lambda(beta, 0)

    return alpha