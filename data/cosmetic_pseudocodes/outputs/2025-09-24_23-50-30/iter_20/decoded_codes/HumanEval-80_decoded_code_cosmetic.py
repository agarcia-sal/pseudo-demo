from typing import Sequence

def is_happy(phi: Sequence[str]) -> bool:
    delta: int = len(phi)
    if delta < 3:
        return False
    omega: int = 0
    while omega <= delta - 3:
        xi = phi[omega]
        upsilon = phi[omega + 1]
        tau = phi[omega + 2]
        if xi == upsilon or upsilon == tau or tau == xi:
            return False
        omega += 1
    return True