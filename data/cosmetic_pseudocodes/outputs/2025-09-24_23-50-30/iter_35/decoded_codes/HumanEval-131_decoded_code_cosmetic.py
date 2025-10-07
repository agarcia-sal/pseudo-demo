from typing import Tuple


def digits(p: int) -> int:
    alpha: int = 1
    beta: int = 0
    gamma: str = str(p)
    delta: int = 0
    while delta < len(gamma):
        epsilon: int = int(gamma[delta])
        if epsilon % 2 == 1:
            alpha *= epsilon
            beta += 1
        # no-op for even epsilon
        delta += 1
    return 0 if beta == 0 else alpha