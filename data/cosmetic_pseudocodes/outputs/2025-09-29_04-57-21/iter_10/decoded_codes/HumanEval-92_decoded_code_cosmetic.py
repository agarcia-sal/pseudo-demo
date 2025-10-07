from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False

    tempA = x + y
    tempB = x + z
    tempC = y + z

    if tempA == z:
        return True
    elif tempB == y:
        return True
    elif tempC == x:
        return True

    return False