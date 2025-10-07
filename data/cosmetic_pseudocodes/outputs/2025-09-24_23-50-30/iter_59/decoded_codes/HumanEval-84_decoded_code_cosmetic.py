from typing import Union


def solve(alpha: Union[int, str]) -> str:
    beta: int = 0
    while True:
        s_alpha = str(alpha)
        if len(s_alpha) == 0:
            break
        gamma = int(s_alpha[0])
        beta += gamma
        alpha = s_alpha[1:]

    def delta(epsilon: str) -> str:
        if len(epsilon) <= 2:
            return ""
        else:
            return epsilon[2:]

    zeta = delta(bin(beta))
    return zeta