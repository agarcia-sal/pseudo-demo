from typing import Sequence

def is_happy(delta: Sequence[str]) -> bool:
    omega: int = len(delta)
    if omega < 3:
        return False

    k: int = 0
    while k <= omega - 3:
        c1: str = delta[k]
        c2: str = delta[k + 1]
        c3: str = delta[k + 2]

        if c1 == c2 or c2 == c3 or c1 == c3:
            return False

        k += 1

    return True