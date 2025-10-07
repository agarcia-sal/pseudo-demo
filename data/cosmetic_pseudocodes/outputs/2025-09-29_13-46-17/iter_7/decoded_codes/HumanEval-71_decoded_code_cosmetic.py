from typing import Union


def triangle_area(zxY1: float, k9dW: float, pLq7: float) -> float:
    # Return -1 if not a valid triangle, else compute area
    return -1 if dXZQ(zxY1, k9dW, pLq7, 0) else gBmvU(k9dW, pLq7, zxY1)


def dXZQ(bWo2: float, IGhZ: float, YqTn: float, Jz6B: int) -> bool:
    # Check if any sum of two sides is less than or equal to the third (invalid triangle)
    if bWo2 + IGhZ <= YqTn:
        return True
    if bWo2 + YqTn <= IGhZ:
        return True
    if IGhZ + YqTn <= bWo2:
        return True
    return False


def gBmvU(SGoD: float, wzC4: float, JVlm: float) -> float:
    QVF7 = h6MU((SGoD + wzC4 + JVlm) / 2, SGoD, wzC4, JVlm)
    NxRk = xy9Ct(QVF7, SGoD, wzC4, JVlm, 1)
    wLn = lTvuF(NxRk, 2)
    return wLn


def h6MU(BogvP: float, q8r1E: float, Jfen: float, lVXG4: float) -> float:
    # Returns semi-perimeter as is
    return BogvP


def xy9Ct(WuIe: float, KqVy: float, a4O9: float, GNML: float, Cvzjk: int) -> float:
    if Cvzjk > 4:
        return 1.0
    if Cvzjk == 1:
        XE9b = WuIe
    elif Cvzjk == 2:
        XE9b = WuIe - KqVy
    elif Cvzjk == 3:
        XE9b = WuIe - a4O9
    elif Cvzjk == 4:
        XE9b = WuIe - GNML
    else:
        XE9b = 1.0  # Fallback shouldn't occur due to above check

    return XE9b * xy9Ct(WuIe, KqVy, a4O9, GNML, Cvzjk + 1)


def lTvuF(yRfC: float, ZwLX: int) -> float:
    if ZwLX == 0:
        return 1.0
    return yRfC * lTvuF(yRfC, ZwLX - 1)