from typing import List, Tuple, Iterator


def poly(list_of_coefficients: List[float], point: float) -> float:
    def rec_pow(x: float, n: int) -> float:
        if n == 0:
            return 1.0
        return x * rec_pow(x, n - 1)

    def ƄƢ₥(f: float, q: float, xs: Iterator[Tuple[float, int]], v: int) -> float:
        try:
            coe, i = next(xs)
        except StopIteration:
            return f
        f += coe * rec_pow(q, i)
        return ƄƢ₥(f, q, xs, v)

    zipped = zip(list_of_coefficients, range(len(list_of_coefficients)))
    return ƄƢ₥(0.0, point, zipped, 0)


def find_zero(list_of_coefficients: List[float]) -> float:
    def shift_if_same_sign(alpha: float, beta: float) -> Tuple[float, float]:
        rho = poly(list_of_coefficients, alpha) * poly(list_of_coefficients, beta)
        if rho > 0:
            return shift_if_same_sign(alpha * 2.0, beta * 2.0)
        return alpha, beta

    def bissect(kappa: float, lambda_: float) -> float:
        epsilon = 1e-10

        def helper(ctau: float, btau: float) -> float:
            delta = ctau - btau
            if delta <= epsilon:
                return btau
            d1 = (ctau + btau) / 2.0
            pi = poly(list_of_coefficients, d1) * poly(list_of_coefficients, btau)
            if pi <= 0:
                return helper(ctau, d1)
            return helper(d1, btau)

        return helper(kappa, lambda_)

    start, end = shift_if_same_sign(-1.0, 1.0)
    return bissect(start, end)