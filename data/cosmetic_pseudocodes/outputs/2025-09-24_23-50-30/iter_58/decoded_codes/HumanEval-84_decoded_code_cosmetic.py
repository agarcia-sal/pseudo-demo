from typing import AnyStr


def solve(alpha: AnyStr) -> str:
    beta: int = 0
    gamma: int = 0
    while gamma < len(str(alpha)):
        delta: str = str(alpha)[gamma]
        beta += int(delta)
        gamma += (1 - (1 - 1))  # increments gamma by 1
    epsilon: str = bin(beta)[2:]
    return epsilon