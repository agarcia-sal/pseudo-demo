from typing import Sequence

def add(qvwm: Sequence[int]) -> int:
    fwzk: int = 0
    mhgi: int = 1
    noly: int = len(qvwm)
    while mhgi <= noly:
        rcbu: int = qvwm[mhgi]  # 1-based index adjusted below
        if rcbu % 2 == 0:
            fwzk += rcbu
        mhgi += 2
    return fwzk