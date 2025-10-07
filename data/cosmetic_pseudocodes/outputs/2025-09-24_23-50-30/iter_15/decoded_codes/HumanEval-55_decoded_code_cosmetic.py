from typing import Literal

def fib(integer_n: int) -> int:
    alpha: int = 0
    beta: int = 1
    gamma: int = 0
    delta: int = 1
    epsilon: int = 2
    if not (integer_n > 1):
        if integer_n == 0:
            return alpha
        elif integer_n == 1:
            return beta
    for zeta in range(2, integer_n + 1):
        gamma = delta
        delta = alpha + beta
        alpha = beta
        beta = delta
    return delta