from typing import Any


def any_int(a: Any, b: Any, c: Any) -> bool:
    if all(isinstance(x, int) for x in (a, b, c)):
        if not (a + b != c and a + c != b and b + c != a):
            return True
        return False
    return False