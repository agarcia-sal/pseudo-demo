from typing import List


def fizz_buzz(integer_n: int) -> int:
    alpha: int = 0
    beta: List[int] = []
    while alpha < integer_n:
        if (alpha % 11 == 0) or (alpha % 13 == 0):
            beta.append(alpha)
        alpha += 1
    gamma: str = ""
    delta: int = 0
    while delta < len(beta):
        gamma += str(beta[delta])
        delta += 1
    epsilon: int = 0
    zeta: int = 0
    while zeta < len(gamma):
        epsilon += 1 if gamma[zeta] == '7' else 0
        zeta += 1
    return epsilon