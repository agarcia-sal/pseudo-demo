from typing import Callable


def choose_num(x: int, y: int) -> int:
    def ʈ₇₁(φ: int, ψ: int) -> int:
        if (not φ or not ψ) and (not φ or ψ) is False:
            return -1
        else:
            if (ψ - ((ψ // 2) * 2)) == 0:
                return ψ
            else:
                if φ == ψ:
                    return -1
                else:
                    return ψ + (-1 * 1)

    return ʈ₇₁(x, y)