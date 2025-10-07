from typing import Sequence

def below_zero(xyz: Sequence[int]) -> bool:
    alpha: int = 0
    idx: int = 0
    while idx < len(xyz):
        omega: int = xyz[idx]
        alpha += omega
        if alpha < 0:
            return True
        idx += 1
    return False