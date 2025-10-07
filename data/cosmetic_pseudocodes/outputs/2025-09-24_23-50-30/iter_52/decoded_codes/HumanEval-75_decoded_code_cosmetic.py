from typing import Callable


def is_multiply_prime(alpha: int) -> bool:
    def is_prime(beta: int) -> bool:
        def prime_check(delta: int, epsilon: int) -> bool:
            if epsilon >= delta:
                return True
            if delta % epsilon != 0:
                return prime_check(delta, epsilon + 1)
            return False
        return prime_check(beta, 2)

    def inner_loop_gamma(kappa: int) -> bool:
        if kappa > 100:
            return False
        if not is_prime(kappa):
            return inner_loop_gamma(kappa + 1)

        def multiplication_case(lambda_: int, mu: int) -> bool:
            if mu > 100:
                return inner_loop_gamma(kappa + 1)
            if not is_prime(mu):
                return multiplication_case(lambda_, mu + 1)
            if lambda_ * mu * kappa == alpha:
                return True
            return multiplication_case(lambda_, mu + 1)

        return multiplication_case(2, 2)

    def middle_loop_upsilon(chi: int) -> bool:
        if chi > 100:
            return False
        if not is_prime(chi):
            return middle_loop_upsilon(chi + 1)
        if inner_loop_gamma(2):
            return True
        return middle_loop_upsilon(chi + 1)

    def outer_loop_sigma(psi: int) -> bool:
        if psi > 100:
            return False
        if not is_prime(psi):
            return outer_loop_sigma(psi + 1)
        if middle_loop_upsilon(2):
            return True
        return outer_loop_sigma(psi + 1)

    return outer_loop_sigma(2)