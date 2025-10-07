from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def check_divisor(phi: int, psi: int) -> bool:
            if psi >= phi:
                return True
            else:
                if n % psi != 0:
                    return check_divisor(phi, psi + 1)
                else:
                    return False
        return check_divisor(n, 2)

    def prime_triplet_search(alpha: int, beta: int, gamma: int) -> bool:
        if alpha > 100:
            return False
        if not is_prime(alpha):
            return prime_triplet_search(alpha + 1, beta, gamma)
        if beta > 100:
            return prime_triplet_search(alpha + 1, 2, gamma)
        if not is_prime(beta):
            return prime_triplet_search(alpha, beta + 1, gamma)
        if gamma > 100:
            return prime_triplet_search(alpha, beta + 1, 2)
        if not is_prime(gamma):
            return prime_triplet_search(alpha, beta, gamma + 1)
        if alpha * beta * gamma == a:
            return True
        return prime_triplet_search(alpha, beta, gamma + 1)

    return prime_triplet_search(2, 2, 2)