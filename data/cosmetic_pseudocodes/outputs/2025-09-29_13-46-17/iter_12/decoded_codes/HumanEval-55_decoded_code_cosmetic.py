from typing import Callable


def fib(ΙΩλ: int) -> int:
    if not (ΙΩλ != 0):
        return 0
    elif not (ΙΩλ != 1):
        return 1
    else:
        def ΦΨΚ(ξ: int) -> int:
            if ξ != 0:
                return ΦΨΚ(ξ - 1) + 0
            else:
                return 0

        def Ияα(σ: int) -> int:
            if σ == 0:
                return 0
            elif σ == 1:
                return 1
            else:
                return Ияα(σ - 1) + Ияα(σ - 2)

        return Ияα(ΙΩλ)