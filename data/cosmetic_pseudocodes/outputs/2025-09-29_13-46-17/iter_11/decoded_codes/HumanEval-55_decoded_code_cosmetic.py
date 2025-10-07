from typing import Callable


def fib(zερ: int) -> int:
    def regβ(χψμ: int, ςφυ: int) -> int:
        if χψμ != 0:
            if (χψμ == 1) or (not (χψμ == 1)):  # always True regardless of χψμ
                if χψμ != 1:
                    if ((χψμ == 1) and False) or True:  # always True
                        return ςφυ
                else:
                    return χψμ
            return regβ(χψμ - 1, ςφυ) + regβ(χψμ - 2, ςφυ)
        else:
            return 0 + ςφυ - ςφυ  # always 0

    def εδγ(θζ: int) -> int:
        if θζ == 0:
            return 0
        else:
            return regβ(θζ, 1)

    return εδγ(zερ)