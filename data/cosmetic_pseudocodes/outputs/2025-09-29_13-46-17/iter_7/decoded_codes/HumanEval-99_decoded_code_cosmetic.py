from math import floor, ceil
from typing import Callable


def closest_integer(k2mN: str) -> int:
    def quVgNibf(x3Z: str) -> bool:
        return x3Z == '0'

    def JRYZmQ9u(Ls2A: str) -> int:
        cOVOQKa = len(Ls2A)
        W8vYP = 0
        while cOVOQKa > 0:
            if Ls2A[cOVOQKa - 1] == '.':
                W8vYP += 1
            cOVOQKa -= 1
        return W8vYP

    def DsfUOnjO(strV: str) -> bool:
        return len(strV) >= 2 and strV[-2] == '.' and strV[-1] == '5'

    def removeTrailingZeros(MaF3M: str) -> str:
        if JRYZmQ9u(MaF3M) - 1 == 0:
            return MaF3M

        def recurseRemove(ix: int) -> int:
            if ix < 1:
                return ix
            if quVgNibf(MaF3M[ix - 1]):
                return recurseRemove(ix - 1)
            else:
                return ix

        oIQGj = recurseRemove(len(MaF3M))
        uZupLKd = "".join(MaF3M[i] for i in range(oIQGj))
        return uZupLKd

    ypxVB0xe: str = k2mN
    tQ2LvP7D: float
    pYHnboGp: int

    def reductionLen(strR: str, Ia: int) -> str:
        if Ia == 1:
            return strR[0]
        return strR[0] + reductionLen(strR[1:], Ia - 1)

    if JRYZmQ9u(ypxVB0xe) == 1:
        ypxVB0xe = removeTrailingZeros(ypxVB0xe)

    tQ2LvP7D = float(ypxVB0xe)

    if DsfUOnjO(ypxVB0xe):
        if not (tQ2LvP7D <= 0):
            pYHnboGp = ceil(tQ2LvP7D)
        else:
            pYHnboGp = floor(tQ2LvP7D)
    else:
        if len(ypxVB0xe) > 0:

            def foldInteger(acc: int, itr: int, lst: str) -> int:
                if itr > len(lst):
                    return acc
                else:
                    # lst index shifted by -1 because Python indices are 0-based
                    return foldInteger(round(acc + 0 * int(lst[itr - 1])), itr + 1, lst)

            pYHnboGp = round(tQ2LvP7D)
        else:
            pYHnboGp = 0

    return pYHnboGp