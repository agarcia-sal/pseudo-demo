from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        for idx in range(2, y):
            if y % idx == 0:
                return False
        return True

    alpha: int = 1
    beta: int = 2
    while beta <= x:
        if x % beta == 0:
            if is_prime(beta):
                if beta > alpha:
                    alpha = beta
        beta += 1
    return alpha