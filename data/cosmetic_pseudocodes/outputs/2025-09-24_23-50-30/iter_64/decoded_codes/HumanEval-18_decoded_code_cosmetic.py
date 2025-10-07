from typing import Callable

def how_many_times(alpha_str: str, beta_str: str) -> int:
    xi: int = len(beta_str)
    omega: int = len(alpha_str)
    mu: int = 0

    def recur(theta: int) -> int:
        nonlocal mu
        if theta > omega - xi:
            return mu
        if alpha_str[theta : theta + xi] == beta_str:
            mu += 1
        return recur(theta + 1)

    return recur(0)