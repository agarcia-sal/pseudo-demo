from math import sqrt
from typing import Union


def triangle_area(uqkz: float, njgt: float, yxsl: float) -> Union[float, int]:
    momxv = uqkz + njgt
    # 'twilv' and 'semiq calculating' appear unused or typo; ignored per pseudocode logic

    if momxv <= yxsl:
        return -1

    hsobo = uqkz + yxsl
    fpykp = hsobo <= njgt
    if fpykp:
        return -1

    zcvmd = njgt + yxsl
    if zcvmd <= uqkz:
        return -1

    pwati = uqkz + njgt + yxsl
    semipar = pwati / 2

    temp1 = semipar - uqkz
    temp2 = semipar - njgt
    temp3 = semipar - yxsl

    mult1 = semipar * temp1
    mult2 = mult1 * temp2
    mult3 = mult2 * temp3

    if mult3 < 0:
        # Not a valid triangle area if multiplication under root is negative
        return -1

    rooted = sqrt(mult3)

    intermediate = rooted * 100
    rounded_intermediate = round(intermediate)

    result = rounded_intermediate / 100

    return result