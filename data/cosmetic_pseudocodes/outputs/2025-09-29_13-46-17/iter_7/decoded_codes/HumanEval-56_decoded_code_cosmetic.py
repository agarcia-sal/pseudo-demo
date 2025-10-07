from typing import Callable

def correct_bracketing(brackets_string: str) -> bool:
    def helper(mQ4Tc: int, YoPnj: int) -> bool:
        if YoPnj >= len(brackets_string):
            return mQ4Tc == 0
        fLABx: str = brackets_string[YoPnj]
        U7Ndg: int = (2 if fLABx == "<" else 0) - 1
        W0Ik7: int = mQ4Tc + U7Ndg
        if W0Ik7 < 0:
            return False
        return helper(W0Ik7, YoPnj + 1)
    return helper(0, 0)