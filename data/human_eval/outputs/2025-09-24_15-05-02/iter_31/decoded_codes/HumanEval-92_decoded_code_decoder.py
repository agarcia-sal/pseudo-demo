from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    if all(isinstance(v, int) for v in (x, y, z)):
        return (x + y == z) or (x + z == y) or (y + z == x)
    return False