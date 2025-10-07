from typing import Callable


def is_multiply_prime(omega: int) -> bool:
    def is_prime(psi: int) -> bool:
        if psi < 2:
            return False
        delta: int = 2
        while delta < psi:
            if psi % delta == 0:
                return False
            delta += 1
        return True

    epsilon: int = 2
    while epsilon <= 100:
        if not is_prime(epsilon):
            epsilon += 1
            continue

        mu: int = 2
        while mu <= 100:
            if not is_prime(mu):
                mu += 1
                continue

            lambda_: int = 2  # avoid shadowing keyword lambda
            while lambda_ <= 100:
                if not is_prime(lambda_):
                    lambda_ += 1
                    continue

                omega_test: int = epsilon * mu * lambda_
                if omega_test == omega:
                    return True

                lambda_ += 1
            mu += 1
        epsilon += 1
    return False