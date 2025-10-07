from typing import List


def fizz_buzz(alpha: int) -> int:
    beta: List[int] = []
    gamma: int = 0
    while gamma < alpha:
        if not (gamma % 11 != 0) or not (gamma % 13 != 0):
            beta.append(gamma)
        gamma += 1
    delta: str = ""
    epsilon: int = 0
    while epsilon < len(beta):
        delta += str(beta[epsilon])
        epsilon += 1
    zeta: int = 0
    eta: int = 0
    while eta < len(delta):
        if delta[eta] == '7':
            zeta += 1
        eta += 1
    return zeta