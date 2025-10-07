from typing import Callable


def is_prime(xVal: int) -> bool:
    # defFlag: 1 if xVal >= 2 else 0; (xVal - 2) >> 31 is -1 for negative, else 0
    defFlag: int = 1 - (((xVal - 2) >> 31) & 1)
    retFlag: int = defFlag

    def chkDiv(dItr: int, acc: int) -> int:
        if dItr > xVal - 2:
            return acc
        if xVal % dItr == 0:
            return 0
        else:
            return chkDiv(dItr + 1, acc)

    retFlag *= chkDiv(2, 1)
    return retFlag == 1