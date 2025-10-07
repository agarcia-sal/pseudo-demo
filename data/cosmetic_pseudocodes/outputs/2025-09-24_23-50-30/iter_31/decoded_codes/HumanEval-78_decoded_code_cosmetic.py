from typing import Set


def hex_key(beta: str) -> int:
    epsilon: Set[str] = {'D', '5', '7', '3', 'B', '2'}
    zeta: int = 0
    eta: int = 0
    length: int = len(beta)
    while eta <= length - 1:
        if beta[eta] in epsilon:
            zeta += 1
        eta += 1
    return zeta