from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return (x + y) == z or (x + z) == y or (y + z) == x
    return False