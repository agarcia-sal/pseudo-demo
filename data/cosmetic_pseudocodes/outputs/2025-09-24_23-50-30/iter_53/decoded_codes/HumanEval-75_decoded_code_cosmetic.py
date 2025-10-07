from typing import Callable

def is_multiply_prime(alpha: int) -> bool:
    def is_prime(beta: int) -> bool:
        def check_division(gamma: int, delta: int) -> bool:
            if delta >= gamma:
                return True
            if gamma % delta == 0:
                return False
            return check_division(gamma, delta + 1)
        return check_division(beta, 2)

    def iterate_i(epsilon: int) -> bool:
        if epsilon > 100:
            return False
        if not is_prime(epsilon):
            return iterate_i(epsilon + 1)

        def iterate_j(zeta: int) -> bool:
            if zeta > 100:
                return iterate_i(epsilon + 1)
            if not is_prime(zeta):
                return iterate_j(zeta + 1)

            def iterate_k(eta: int) -> bool:
                if eta > 100:
                    return iterate_j(zeta + 1)
                if not is_prime(eta):
                    return iterate_k(eta + 1)
                if epsilon * zeta * eta == alpha:
                    return True
                return iterate_k(eta + 1)

            return iterate_k(2)

        return iterate_j(2)

    return iterate_i(2)