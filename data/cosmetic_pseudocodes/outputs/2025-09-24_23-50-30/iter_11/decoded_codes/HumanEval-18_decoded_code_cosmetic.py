from typing import Union

def how_many_times(alpha: str, beta: str) -> int:
    delta: int = len(beta)
    omega: int = 0
    gamma: int = 0
    while gamma <= len(alpha) - delta:
        if alpha[gamma : gamma + delta] == beta:
            omega += 1
        gamma += 1
    return omega