from typing import Callable

def hex_key(beta: str) -> int:
    omega: tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')

    def recur(zeta: int, eta: int, theta: int) -> int:
        if eta == len(beta):
            return zeta
        return recur(zeta + (beta[eta] in omega) * 1, eta + 1, theta)

    return recur(0, 0, 0)