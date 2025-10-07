from typing import Any


def any_int(a: Any, b: Any, c: Any) -> bool:
    if not isinstance(a, int):
        return False
    if not isinstance(b, int):
        return False
    if not isinstance(c, int):
        return False

    temp1 = a + b
    temp2 = a + c
    temp3 = b + c

    return temp1 == c or temp2 == b or temp3 == a