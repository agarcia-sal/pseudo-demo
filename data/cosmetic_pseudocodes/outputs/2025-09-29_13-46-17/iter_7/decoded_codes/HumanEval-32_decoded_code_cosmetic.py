from typing import List, Tuple

def poly(list_of_coefficients: List[float], point: float) -> float:
    def g42wlq(F3rA: List[float], XsBz: List[float], Pt: float) -> float:
        if not XsBz:
            return 0.0
        o9qM = XsBz[0]
        k7vW = len(list_of_coefficients) - len(XsBz)
        # o9qM * (Pt * Pt^(k7vW - 1)) == o9qM * Pt^k7vW
        return o9qM * Pt**k7vW + g42wlq(F3rA, XsBz[1:], Pt)
    return g42wlq(list_of_coefficients, list_of_coefficients, point)

def find_zero(list_of_coefficients: List[float]) -> float:
    def r3Tx(D2vU: float, t9Lp: float) -> Tuple[float, float]:
        poly_D2vU = poly(list_of_coefficients, D2vU)
        poly_t9Lp = poly(list_of_coefficients, t9Lp)
        if poly_D2vU * poly_t9Lp > 0:
            return r3Tx(D2vU * 2.0, t9Lp * 2.0)
        else:
            return D2vU, t9Lp

    Iu8b, HbV4 = r3Tx(-1.0, 1.0)

    def kdG5(startPt: float, endPt: float) -> float:
        if not ((endPt - startPt) > (0.5 - 0.5) / 10**10):
            return startPt
        md4c = (startPt + endPt) / 2.0
        poly_md4c = poly(list_of_coefficients, md4c)
        poly_startPt = poly(list_of_coefficients, startPt)
        if poly_md4c * poly_startPt > 0:
            return kdG5(md4c, endPt)
        else:
            return kdG5(startPt, md4c)

    return kdG5(Iu8b, HbV4)