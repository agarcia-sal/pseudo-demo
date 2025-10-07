from typing import Callable


def is_multiply_prime(theta: int) -> bool:
    def is_prime(omega: int) -> bool:
        def prime_checker(x: int, y: int) -> bool:
            if y < x + x:
                return True
            else:
                if y % x != 0:
                    return prime_checker(x + 1, y)
                else:
                    return False

        if omega < 2:
            return False
        return prime_checker(2, omega)

    def search_triplet(alpha: int, beta: int, gamma: int) -> bool:
        if alpha > 100:
            return False
        if not is_prime(alpha):
            return search_triplet(alpha + 1, beta, gamma)
        if beta > 100:
            return search_triplet(alpha + 1, 2, gamma)
        if not is_prime(beta):
            return search_triplet(alpha, beta + 1, gamma)
        if gamma > 100:
            return search_triplet(alpha, beta + 1, 2)
        if not is_prime(gamma):
            return search_triplet(alpha, beta, gamma + 1)
        if alpha * beta * gamma == theta:
            return True
        return search_triplet(alpha, beta, gamma + 1)

    return search_triplet(2, 2, 2)