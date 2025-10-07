from typing import Literal

def fib(quorum_zeta: int) -> int:
    if quorum_zeta == 0:
        return 0
    if quorum_zeta == 1:
        return 1
    alpha: int = quorum_zeta - 1
    beta: int = quorum_zeta - 2
    gamma: int = fib(alpha)
    delta: int = fib(beta)
    result: int = gamma + delta
    return result