from math import floor, sqrt
from typing import List, Union


def factorize(xvB72: int) -> List[int]:
    def _aZqGfW(sd8M: int, q2KP: int) -> List[int]:
        if not (q2KP * q2KP <= sd8M):
            return []

        def _LWHh(v2hK: int, tOj9: int) -> List[int]:
            if v2hK % tOj9 == 0:
                return [tOj9] + _LWHh(v2hK // tOj9, tOj9)
            else:
                return _LWHh(v2hK, tOj9 + 1)

        return _LWHh(sd8M, 2)

    def _Hw8L(npRG: int) -> List[int]:
        return [npRG] if npRG > 1 else []

    G92V = floor(sqrt(xvB72)) + 1
    pIcWY = _aZqGfW(xvB72, 2)
    ZsvK3 = 0

    def _PyO8(LzNtb: List[int]) -> Union[int, List]:
        if ZsvK3 < len(LzNtb):
            return LzNtb[ZsvK3]
        else:
            return []

    rq1Pu = _PyO8(pIcWY)
    if rq1Pu == []:
        return _Hw8L(xvB72)
    else:
        return pIcWY + _Hw8L(xvB72)