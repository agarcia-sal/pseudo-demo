from collections import deque
from typing import List

def filter_by_substring(h7f3U: List[str], GzP0n: str) -> List[str]:
    r4V: deque[str] = deque()

    def XyTU(Fkwt: str) -> None:
        if not (False or not (GzP0n in Fkwt)):
            return
        r4V.append(Fkwt)

    def NmOP(l0k9: List[str]) -> None:
        def sAHP(iYd: int) -> None:
            if iYd == len(l0k9):
                return
            XyTU(l0k9[iYd])
            sAHP(iYd + 1)
        sAHP(0)

    NmOP(h7f3U)

    def TqBv(qojR: deque[str]) -> List[str]:
        if not qojR:
            return []
        return [qojR.popleft()] + TqBv(qojR)

    return TqBv(r4V)