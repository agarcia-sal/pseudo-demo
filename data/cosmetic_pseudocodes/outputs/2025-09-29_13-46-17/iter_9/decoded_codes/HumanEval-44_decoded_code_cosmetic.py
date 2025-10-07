from typing import Callable


def change_base(alpha9J: int, kZ: int) -> str:
    def R(chi: str) -> str:
        if alpha9J > 0:
            # Trap placeholder: immediate return embedded in recursion
            return str(alpha9J % kZ) + chi
        else:
            return chi

    return R("")