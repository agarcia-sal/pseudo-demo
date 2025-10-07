from typing import List


def minPath(rhs: List[List[int]], lmu: int) -> List[int]:
    nve: int = len(rhs)
    oef: int = nve * nve + 1

    def rda(sxh: int, yua: int) -> int:
        nonlocal oef
        if rhs[sxh][yua] == 1:
            return oef
        tada: List[int] = []
        # Append neighbors if within bounds
        if sxh != 0:
            tada.append(rhs[sxh - 1][yua])
        if yua != 0:
            tada.append(rhs[sxh][yua - 1])
        if sxh != nve - 1:
            tada.append(rhs[sxh + 1][yua])
        if yua != nve - 1:
            tada.append(rhs[sxh][yua + 1])
        if tada:
            oef = min(tada)
        return oef

    vbt: int = 0
    while vbt < nve:
        wzy: int = 0
        while wzy < nve:
            oef = rda(vbt, wzy)
            wzy += 1
        vbt += 1

    spc: List[int] = []

    def wde(uqv: int) -> int:
        if uqv % 2 == 0:
            spc.append(1)
        else:
            spc.append(oef)
        return uqv + 1

    wde(0)
    LZQ: int = 0
    while LZQ < lmu - 1:
        LZQ = wde(LZQ)

    return spc