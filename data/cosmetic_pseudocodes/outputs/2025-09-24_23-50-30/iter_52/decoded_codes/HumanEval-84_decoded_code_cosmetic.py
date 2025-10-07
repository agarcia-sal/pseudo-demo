from typing import Callable


def solve(alpha: int) -> str:
    beta: int = 0

    def via_index(gamma: str, delta: int) -> int:
        if delta == len(gamma):
            return 0
        return int(gamma[delta]) + via_index(gamma, delta + 1)

    beta = via_index(str(alpha), 0)
    epsilon = bin(beta)[2:]
    return epsilon