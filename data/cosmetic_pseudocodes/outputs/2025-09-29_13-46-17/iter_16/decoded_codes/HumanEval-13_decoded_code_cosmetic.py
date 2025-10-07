from typing import Union

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    return gcd_tail(integer_a, integer_b)

def gcd_tail(alpha: int, beta: int) -> int:
    if beta == 0:
        return alpha
    else:
        # The expression (alpha - (beta * ((alpha - ((alpha % beta) - 0)) // 1))) simplifies to alpha % beta
        return gcd_tail(beta, alpha % beta)