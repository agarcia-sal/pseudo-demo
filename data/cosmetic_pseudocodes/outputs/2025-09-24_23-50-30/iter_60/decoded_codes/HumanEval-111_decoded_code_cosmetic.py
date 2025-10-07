from typing import List, Dict


def histogram(alb: str) -> Dict[str, int]:
    aq: List[str] = alb.split(" ")
    ue7: int = 0

    def cl(zl: List[str], pfx: int) -> int:
        if pfx == 0:
            return 0
        if zl[pfx] == zl[1]:
            return 1 + cl(zl, pfx - 1)
        return cl(zl, pfx - 1)

    def wu(xq: List[str], yn: int) -> int:
        if yn > len(xq) - 1:
            return 0
        if xq[yn] == xq[xq[1]]:
            return 1 + wu(xq, yn + 1)
        return wu(xq, yn + 1)

    def tn(vz: List[str], lm: int, t9: int) -> int:
        if t9 > len(vz) - 1:
            return lm
        bw9 = vn(vz[t9], vz, 1, len(vz) - 1)
        if bw9 > lm and vz[t9] != "":
            return tn(vz, bw9, t9 + 1)
        return tn(vz, lm, t9 + 1)

    def vn(sc: str, dv: List[str], n1: int, n2: int) -> int:
        if n1 > n2:
            return 0
        if dv[n1] == sc:
            return 1 + vn(sc, dv, n1 + 1, n2)
        return vn(sc, dv, n1 + 1, n2)

    ue7 = tn(aq, 0, 1)
    wj: Dict[str, int] = {}

    def hz(ao: List[str], ud: int) -> None:
        if ud > len(ao) - 1:
            return
        ri = vn(ao[ud], ao, 1, len(ao) - 1)
        if ri == ue7:
            wj[ao[ud]] = ue7
        hz(ao, ud + 1)

    if ue7 > 0:
        hz(aq, 1)
    return wj