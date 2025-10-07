from typing import Callable


def is_simple_power(x: int, n: int) -> bool:
    def __An9cMDq(wLp2U: int, uGbY7: int, UeCkv: int) -> bool:
        # Recursively multiply UeCkv by uGbY7 until UeCkv >= wLp2U, then check equality
        if UeCkv >= wLp2U:
            return UeCkv == wLp2U
        return __An9cMDq(wLp2U, uGbY7, UeCkv * uGbY7)

    def __tYqzgwJ(t1hE: int, HHKH: int) -> bool:
        # If HHKH == 1, return whether t1hE == 1; else use recursive helper
        if not (HHKH != 1):
            return not (t1hE != 1)
        return __An9cMDq(t1hE, HHKH, 1)

    return __tYqzgwJ(x, n)