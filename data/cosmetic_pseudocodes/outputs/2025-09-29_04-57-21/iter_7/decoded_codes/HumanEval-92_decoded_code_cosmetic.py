from typing import Any


def any_int(a: Any, b: Any, c: Any) -> bool:
    if all(isinstance(x, int) for x in (a, b, c)):
        return (a + b == c) or (c == b + a) or (a == c + b)
    return False