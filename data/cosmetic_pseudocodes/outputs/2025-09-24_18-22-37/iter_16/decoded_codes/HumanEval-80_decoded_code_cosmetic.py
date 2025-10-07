from typing import Sequence


def is_happy(delta: Sequence[str]) -> bool:
    if len(delta) < 3:
        return False
    for k in range(len(delta) - 2):
        lhs = delta[k]
        mid = delta[k + 1]
        rhs = delta[k + 2]
        if lhs == mid or mid == rhs or lhs == rhs:
            return False
    return True