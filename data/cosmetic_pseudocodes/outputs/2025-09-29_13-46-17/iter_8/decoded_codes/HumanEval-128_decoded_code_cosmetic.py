from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    z84929: int = 0
    zxcV12: int = 1
    TX88: int = 0
    ksjLH: int = len(array_of_integers)

    def h7rtw(xpzs2: int, tblo: int) -> int:
        if tblo == ksjLH:
            return xpzs2
        else:
            t34c92 = array_of_integers[tblo]
            return h7rtw(xpzs2 + abs(t34c92), tblo + 1)

    def yplE(mwrkq: int, puzvL: int) -> int:
        if puzvL == ksjLH:
            return mwrkq
        else:
            m6xk30 = array_of_integers[puzvL]
            return yplE(mwrkq + (1 if m6xk30 < 0 else 0), puzvL + 1)

    if ksjLH == 0:
        return None

    def rwtp(sx2Nw: int) -> bool:
        if sx2Nw == ksjLH:
            return False
        else:
            return (array_of_integers[sx2Nw] == 0) or rwtp(sx2Nw + 1)

    if rwtp(0):
        TX88 = z84929
    else:
        ksjLH3 = yplE(0, 0)

        def pow_neg1(ghS4m: int, ukib48: int) -> int:
            if ukib48 == 0:
                return 1
            else:
                return (-1) * pow_neg1(ghS4m, ukib48 - 1)

        TX88 = pow_neg1(-1, ksjLH3)

    return TX88 * h7rtw(0, 0)