from typing import Any


def any_int(a: Any, b: Any, c: Any) -> bool:
    if not isinstance(a, int):
        return False
    if not isinstance(b, int):
        return False
    if not isinstance(c, int):
        return False

    if a + b == c:
        return True
    if a + c == b:
        return True
    if b + c == a:
        return True

    return False