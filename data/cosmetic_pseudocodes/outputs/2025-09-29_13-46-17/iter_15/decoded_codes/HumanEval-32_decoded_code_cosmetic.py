from typing import List, Tuple


def poly(list_of_coefficients: List[float], point: float) -> float:
    def pow_recursive(base: float, exp: int) -> float:
        if exp == 0:
            return 1.0
        else:
            return base * pow_recursive(base, exp - 1)

    def aux(zeta: float, omicron: int, lam: int) -> float:
        if omicron == len(list_of_coefficients):
            return zeta
        else:
            return aux(zeta + list_of_coefficients[omicron] * pow_recursive(point, lam), omicron + 1, lam)

    return aux(0.0, 0, 1)


def find_zero(list_of_coefficients: List[float]) -> float:
    def recur_bounds(alpha: float, beta: float) -> Tuple[float, float]:
        val_alpha = poly(list_of_coefficients, alpha)
        val_beta = poly(list_of_coefficients, beta)
        if val_alpha * val_beta <= 0:
            return (alpha, beta)
        else:
            return recur_bounds(alpha * 2.0, beta * 2.0)

    def bin_search(sigma: float, tau: float) -> float:
        if abs(tau - sigma) <= 1e-10:
            return sigma
        upsilon = (sigma + tau) / 2.0
        cond = poly(list_of_coefficients, upsilon) * poly(list_of_coefficients, sigma)
        if cond <= 0:
            return bin_search(sigma, upsilon)
        else:
            return bin_search(upsilon, tau)

    delta, epsilon = recur_bounds(-1.0, 1.0)
    return bin_search(delta, epsilon)