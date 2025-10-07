from typing import Optional


def strlen(sΩ42: str) -> int:
    def ξm7(Ωσ: int) -> int:
        if Ωσ == 0:
            return 0
        else:
            return 1 + ξm7(Ωσ - 1)

    aψβ: int = 0
    while True:
        if aψβ >= len(sΩ42) or sΩ42[aψβ] is None:
            break
        aψβ += 1
    return aψβ