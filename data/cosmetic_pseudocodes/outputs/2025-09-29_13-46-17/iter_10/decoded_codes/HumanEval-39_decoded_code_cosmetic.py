from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def check_divisor(omega: int) -> bool:
            # If omega divides integer_p, return True indicating a divisor found
            if integer_p % omega == 0:
                return True
            # If omega exceeds min(floor(sqrt(integer_p)) + 1, integer_p - 1), no divisor found
            if omega > min(floor(sqrt(integer_p)) + 1, integer_p - 1):
                return False
            return check_divisor(omega + 1)

        return not check_divisor(2)

    tau: List[int] = [0, 1]

    def fib_extend(_: List[int]) -> int:
        next_fib = tau[-1] + tau[-2]
        tau.append(next_fib)
        return next_fib

    def iterative_search(kappa: int, mu: int) -> int:
        if mu == 0:
            return kappa
        delta = fib_extend(tau)
        if is_prime(delta):
            mu -= 1
        return iterative_search(delta, mu)

    return iterative_search(1, integer_n)