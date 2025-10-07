from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    pX: Any = x
    qY: Any = y
    rZ: Any = z

    if not (not isinstance(pX, int) or not isinstance(qY, int) or not isinstance(rZ, int)):
        a_b: int = pX + qY
        c_d: int = pX + rZ
        e_f: int = qY + rZ

        cond_1: bool = not (a_b != rZ)
        cond_2: bool = not (c_d != qY)
        cond_3: bool = not (e_f != pX)

        if cond_1 + cond_2 + cond_3 > 0:
            return True
        return False

    return False