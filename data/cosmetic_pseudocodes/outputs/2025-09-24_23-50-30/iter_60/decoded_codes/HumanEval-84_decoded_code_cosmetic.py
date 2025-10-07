from typing import Callable


def solve(alpha: int) -> str:
    def loop_beta(gamma: int, delta: int) -> int:
        if gamma == len(str(alpha)):
            return delta
        else:
            # char_at at position gamma + 1 (1-based indexing), so index gamma in 0-based
            return loop_beta(gamma + 1, delta + int(str(alpha)[gamma]))

    epsilon = loop_beta(0, 0)

    def to_binary_zeta(eta: int, theta: str) -> str:
        if eta == 0:
            return theta
        else:
            return to_binary_zeta(eta // 2, str(eta % 2) + theta)

    iota = to_binary_zeta(epsilon, "")
    return iota[3:]