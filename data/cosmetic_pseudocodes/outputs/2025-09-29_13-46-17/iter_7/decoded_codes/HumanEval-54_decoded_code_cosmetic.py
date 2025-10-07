from typing import Sequence, List, Optional

def same_chars(z42_QU: Sequence[str], Av9_WK: Sequence[str]) -> bool:
    A1X: List[str] = []

    def QgT2(xP: str) -> None:
        if xP not in A1X:
            A1X.append(xP)

    def VmjG(iJ1: int, size: int) -> Optional[None]:
        if iJ1 >= size:
            return None
        # The original pseudocode uses a lazy AND then condition; here, directly check index and use the element
        QgT2(Av9_WK[iJ1])
        return VmjG(iJ1 + 1, size)

    def fRwH(iV8: int, sz: int) -> Optional[None]:
        if iV8 >= sz:
            return None
        QgT2(z42_QU[iV8])
        return fRwH(iV8 + 1, sz)

    fRwH(0, len(z42_QU))
    VmjG(0, len(Av9_WK))
    return (len(A1X) * 2) == (len(set(z42_QU)) + len(set(Av9_WK)))