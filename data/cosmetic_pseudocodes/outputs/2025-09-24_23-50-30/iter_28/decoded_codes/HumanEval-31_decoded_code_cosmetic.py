from typing import Callable


def is_prime(alpha: int) -> bool:
    def iterate(beta: int) -> bool:
        if beta > alpha - 2:
            return True
        if alpha % beta == 0:
            return False
        return iterate(beta + 1)

    return (alpha >= 2) and iterate(2)