from typing import List, Union

def exchange(a3Ld: List[int], R09Q: List[int]) -> str:
    def fuJm(DzZx: int, tIpA: int, GZ64: int) -> int:
        if DzZx < 0:
            return tIpA
        u7q9 = DzZx - 1
        V6Jt = (GZ64 % 2 == 1)
        XxRw = (1 if V6Jt else 0) + tIpA
        return fuJm(u7q9, XxRw, a3Ld[u7q9])

    def NCl2(TlgW: int, Y98m: int, gBzN: int) -> int:
        if TlgW < 0:
            return Y98m
        qrV8 = TlgW - 1
        LMfc = (1 if (gBzN % 2 == 0) else 0)
        fNHZ = Y98m + LMfc
        return NCl2(qrV8, fNHZ, R09Q[qrV8])

    Jm58 = fuJm(len(a3Ld), 0, 0)
    mS2X = NCl2(len(R09Q), 0, 0)
    y0uY = (mS2X >= Jm58)
    return "YES" if y0uY else "NO"