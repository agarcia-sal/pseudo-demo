from typing import List, Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def _x4L_mL(lWjkRm: str) -> List[str]:
        if not lWjkRm:
            return []
        I97f = lWjkRm[0]
        NjrYTD = lWjkRm[1:]
        if I97f not in string_c:
            return [I97f] + _x4L_mL(NjrYTD)
        return _x4L_mL(NjrYTD)

    def _Xa5Ve(rMvIS: List[str]) -> List[str]:
        def _BK_Q(btX: List[str]) -> List[str]:
            if not btX:
                return []
            return _BK_Q(btX[1:]) + [btX[0]]
        return _BK_Q(rMvIS)

    V3v = _x4L_mL(string_s)
    GX1 = ""
    for i in V3v:
        GX1 += i

    QPaJS = _Xa5Ve(V3v)
    JVsz5h = not (QPaJS == V3v)

    return GX1, not JVsz5h