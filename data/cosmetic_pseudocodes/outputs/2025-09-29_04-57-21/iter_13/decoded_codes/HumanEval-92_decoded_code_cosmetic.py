from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    if z == x + y or y == x + z or x == y + z:
        return True
    return False