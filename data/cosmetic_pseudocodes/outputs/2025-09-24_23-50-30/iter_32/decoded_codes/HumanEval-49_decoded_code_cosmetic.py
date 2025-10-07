from typing import Literal


def modp(integer_n: int, integer_p: int) -> int:
    beta: int = 0
    alpha: int = 1
    while beta < integer_n:
        doubled = alpha * 2
        # Compute alpha = doubled - (doubled // integer_p) * integer_p + (doubled % integer_p)
        alpha = doubled - (doubled // integer_p) * integer_p + (doubled % integer_p)
        alpha %= integer_p
        beta += 1
    return alpha