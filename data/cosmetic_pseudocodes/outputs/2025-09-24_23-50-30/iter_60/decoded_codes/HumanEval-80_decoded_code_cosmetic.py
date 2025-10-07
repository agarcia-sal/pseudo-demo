from typing import Sequence

def is_happy(xyZ: Sequence[str]) -> bool:
    def tailRecursion(etaP: Sequence[str], oLuQ: int) -> bool:
        if oLuQ >= len(etaP) - 2:
            return True
        aBvW = (
            etaP[oLuQ] == etaP[oLuQ + 1] or
            etaP[oLuQ + 1] == etaP[oLuQ + 2] or
            etaP[oLuQ] == etaP[oLuQ + 2]
        )
        if aBvW:
            return False
        return tailRecursion(etaP, oLuQ + 1)

    if len(xyZ) < 3:
        return False
    return tailRecursion(xyZ, 0)