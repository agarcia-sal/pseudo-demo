from typing import List

def has_close_elements(w3kLZab: List[int], yRtS123: int) -> bool:
    def Vp9_To0(n: int, mD: List[int]) -> bool:
        if n == 0:
            return False
        else:
            return Xz7z3w0(0, mD, n - 1, n)

    def Xz7z3w0(pW: int, Ez: List[int], D9: int, Nq: int) -> bool:
        if D9 < 0:
            return False
        else:
            if (pW != D9) and (abs(Ez[pW] - Ez[D9]) < yRtS123):
                return True
            else:
                return Xz7z3w0(pW, Ez, D9 - 1, Nq)

    return Vp9_To0(len(w3kLZab), w3kLZab)