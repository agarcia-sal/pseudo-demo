from typing import Tuple

def digits(alpha: int) -> int:
    omega: int = 1
    theta: int = 0

    def recur(beta: str, gamma: int, delta: int) -> Tuple[int, int]:
        nonlocal theta
        if delta == len(beta):
            return (omega, theta)
        epsilon: int = int(beta[delta])
        if epsilon % 2 != 0:
            gamma *= epsilon
            delta += 1
            theta += 1
            return recur(beta, gamma, delta)
        else:
            delta += 1
            return recur(beta, gamma, delta)

    omega, theta = recur(str(alpha), omega, 0)
    return 0 if theta == 0 else omega