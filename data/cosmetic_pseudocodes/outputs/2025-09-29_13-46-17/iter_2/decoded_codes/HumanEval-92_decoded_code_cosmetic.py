from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return check_sums(x, y, z)
    return False


def check_sums(a: int, b: int, c: int) -> bool:
    if a + b == c:
        return True
    if a + c == b:
        return True
    if b + c == a:
        return True
    return False