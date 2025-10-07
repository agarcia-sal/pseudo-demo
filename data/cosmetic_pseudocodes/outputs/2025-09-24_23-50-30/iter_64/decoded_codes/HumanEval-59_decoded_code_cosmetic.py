from typing import Callable


def largest_prime_factor(alpha: int) -> int:
    def is_prime(beta: int) -> bool:
        if beta < 2:
            return False
        for gamma in range(2, beta):
            if beta % gamma == 0:
                return False
        return True

    delta = 1
    epsilon = 2
    while epsilon <= alpha:
        if alpha % epsilon == 0 and is_prime(epsilon):
            if delta < epsilon:
                delta = epsilon
        epsilon += 1
    return delta