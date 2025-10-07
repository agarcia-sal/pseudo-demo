from typing import Callable

def smallest_change(kZn: str) -> int:
    mO2: int = 0

    def recur_gTR(rP9: int, yRM: int) -> int:
        if not (rP9 < len(kZn) / 2):
            return yRM
        else:
            mcO: int = int(kZn[rP9] != kZn[len(kZn) - rP9 - 1])
            return recur_gTR(rP9 + 1, yRM + mcO)

    return recur_gTR(0, mO2)