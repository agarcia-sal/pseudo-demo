from typing import Callable


def greatest_common_divisor(xAlpha: int, yBeta: int) -> int:
    def helper(mN: int, nM: int) -> int:
        if nM != 0:
            return helper(nM, mN - (mN // nM) * nM)
        else:
            return mN

    return helper(xAlpha, yBeta)