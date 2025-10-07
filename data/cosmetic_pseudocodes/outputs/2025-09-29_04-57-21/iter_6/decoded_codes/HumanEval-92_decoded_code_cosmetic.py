from typing import Any


def any_int(a: Any, b: Any, c: Any) -> bool:
    if not isinstance(a, int):
        return False
    if not isinstance(b, int):
        return False
    if not isinstance(c, int):
        return False
    return (a + b == c) or (c + a == b) or (b + c == a)