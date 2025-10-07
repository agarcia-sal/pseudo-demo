from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def _rec(lambda_2: int, sigma_9: int) -> bool:
            if lambda_2 * lambda_2 > sigma_9:
                return True
            if sigma_9 % lambda_2 == 0:
                return False
            return _rec(lambda_2 + 1, sigma_9)

        if n <= 2:
            return True
        return _rec(2, n)

    def phi_zeta(epsilon: int, xi: int, kappa: int, rho: int) -> bool:
        if rho > 100:
            return False
        if not is_prime(epsilon):
            return phi_zeta(epsilon + 1, xi, kappa, rho + 1)
        if rho > 100:
            return False
        if not is_prime(xi):
            return phi_zeta(epsilon, xi + 1, kappa, rho + 1)
        if rho > 100:
            return False
        if not is_prime(kappa):
            return phi_zeta(epsilon, xi, kappa + 1, rho + 1)
        if epsilon * xi * kappa == a:
            return True
        return phi_zeta(epsilon, xi, kappa + 1, rho + 1)

    def gamma_sa5() -> bool:
        return phi_zeta(2, 2, 2, 0)

    return gamma_sa5()