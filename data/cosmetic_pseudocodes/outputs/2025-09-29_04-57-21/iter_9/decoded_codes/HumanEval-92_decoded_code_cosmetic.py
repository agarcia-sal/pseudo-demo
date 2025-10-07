from typing import Any


def any_int(a: Any, b: Any, c: Any) -> bool:
    if not isinstance(a, int):
        return False
    if not isinstance(b, int):
        return False
    if not isinstance(c, int):
        return False

    if (c == a + b) or (b == a + c) or (a == b + c):
        return True

    return False