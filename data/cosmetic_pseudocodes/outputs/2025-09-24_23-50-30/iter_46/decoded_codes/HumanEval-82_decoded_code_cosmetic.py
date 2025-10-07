from typing import Callable


def prime_length(param_alpha: str) -> bool:
    def check_divisor(param_beta: int) -> bool:
        # If param_beta is greater than len(param_alpha) - 1, no divisors found
        if param_beta > len(param_alpha) - 1:
            return True
        if len(param_alpha) % param_beta != 0:
            return check_divisor(param_beta + 1)
        else:
            return False

    if len(param_alpha) <= 1:
        return False
    else:
        return check_divisor(2)