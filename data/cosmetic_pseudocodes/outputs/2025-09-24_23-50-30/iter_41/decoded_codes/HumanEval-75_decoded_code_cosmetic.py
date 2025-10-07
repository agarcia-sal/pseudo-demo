from typing import Callable


def is_multiply_prime(beta: int) -> bool:
    def is_prime(omega: int) -> bool:
        def check_divisor(delta: int, rho: int) -> bool:
            if rho > delta - 1:
                return True
            if omega % rho == 0:
                return False
            return check_divisor(delta, rho + 1)

        if omega < 2:
            return False
        return check_divisor(omega, 2)

    xi = 2
    while xi <= 100:
        if not is_prime(xi):
            xi += 1
            continue

        psi = 2
        while psi <= 100:
            if not is_prime(psi):
                psi += 1
                continue

            mu = 2
            while mu <= 100:
                if not is_prime(mu):
                    mu += 1
                    continue

                if xi * psi * mu == beta:
                    return True

                mu += 1

            psi += 1

        xi += 1

    return False