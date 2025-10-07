from typing import Union


def any_int(a: object, b: object, c: object) -> bool:
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return False
    return (a + b == c) or (a + c == b) or (b + c == a)