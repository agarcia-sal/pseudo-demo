from typing import Callable


def is_multiply_prime(omega: int) -> bool:
    def is_prime(zeta: int) -> bool:
        def check_divisor(beta: int, gamma: int) -> bool:
            if gamma > beta - 1:
                return True
            if beta % gamma != 0:
                return check_divisor(beta, gamma + 1)
            return False

        if zeta < 2:
            return False  # Handle edge cases: numbers < 2 are not prime
        return check_divisor(zeta, 2)

    def loop_i(mu: int) -> bool:
        if mu > 100:
            return False

        def loop_j(nu: int) -> bool:
            if nu > 100:
                return loop_i(mu + 1)

            def loop_k(xi: int) -> bool:
                if xi > 100:
                    return loop_j(nu + 1)
                return ((not is_prime(xi)) and loop_k(xi + 1)) or \
                       ((is_prime(xi) and ((mu * nu * xi) == omega)) or loop_k(xi + 1))

            return (not is_prime(nu) and loop_j(nu + 1)) or loop_k(2)

        return (not is_prime(mu) and loop_i(mu + 1)) or loop_j(2)

    return loop_i(2)