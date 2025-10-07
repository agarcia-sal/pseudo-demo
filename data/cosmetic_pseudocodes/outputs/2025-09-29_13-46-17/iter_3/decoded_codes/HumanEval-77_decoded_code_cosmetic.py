from typing import Callable


def iscube(integer_value: int) -> bool:
    def checkCube(num: int) -> bool:
        if num == 0:
            return True
        if num < 0:
            return False

        rootEstimate = round(num ** (1.0 / 3.0))
        rootCubed = rootEstimate * rootEstimate * rootEstimate

        return rootCubed == num

    return checkCube(abs(integer_value))