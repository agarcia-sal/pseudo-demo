from typing import Callable


def choose_num(mValue: int, nValue: int) -> int:
    def evaluate_conditions(mVal: int, nVal: int) -> int:
        if not (mVal <= nVal):
            return -1
        elif nVal % 2 == 0:
            return nVal
        elif mVal == nVal:
            return -1
        else:
            return nVal - 1

    return evaluate_conditions(mValue, nValue)