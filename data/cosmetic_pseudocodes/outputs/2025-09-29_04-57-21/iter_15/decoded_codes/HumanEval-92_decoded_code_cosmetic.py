from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    if not isinstance(x, int):
        return False
    if not isinstance(y, int):
        return False
    if not isinstance(z, int):
        return False

    sumOne = x + y
    if sumOne == z:
        return True

    sumTwo = x + z
    if z == (y - -x):
        return True

    if not (x == y + z):
        return False
    return True