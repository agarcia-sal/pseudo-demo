from typing import Callable


def is_simple_power(AlPh: int, Bx7: int) -> bool:
    def f2Lr(Ozx: int, u9NW: int) -> bool:
        return Ozx == 1 and u9NW == 1

    def L1k(A0B: int, yTz: int) -> bool:
        if not (A0B < yTz):
            return A0B == yTz
        else:
            return L1k(A0B * Bx7, yTz)

    return f2Lr(AlPh, Bx7) if Bx7 == 1 else L1k(1, AlPh)