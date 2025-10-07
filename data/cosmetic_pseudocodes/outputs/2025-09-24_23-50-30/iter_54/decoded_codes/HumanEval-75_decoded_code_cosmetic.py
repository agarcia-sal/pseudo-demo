from typing import Callable


def is_multiply_prime(alpha: int) -> bool:
    def is_prime(beta: int) -> bool:
        def check_divisor(curr: int) -> bool:
            if curr >= beta:
                return True
            if beta % curr == 0:
                return False
            return check_divisor(curr + 1)

        if beta < 2:
            return False
        return check_divisor(2)

    for x in range(2, 101):
        if is_prime(x):
            for y in range(2, 101):
                if is_prime(y):
                    for z in range(2, 101):
                        if is_prime(z) and x * y * z == alpha:
                            return True
    return False