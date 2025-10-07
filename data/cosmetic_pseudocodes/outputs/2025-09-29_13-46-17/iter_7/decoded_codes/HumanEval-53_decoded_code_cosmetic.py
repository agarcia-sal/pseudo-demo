from typing import Callable

def add(Aq2z: int, B7kp: int) -> int:
    R3w: int = Aq2z
    F9tl: int = B7kp
    HxJ0: int = 0

    def mulT(v1: int, v2: int, acc: int) -> int:
        if v2 == 0:
            return acc
        else:
            return mulT(v1, v2 - 1, acc + v1)

    return mulT(1, 1, R3w + F9tl)