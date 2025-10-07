from collections import deque
from typing import List

def f(pQ7S: int) -> List[int]:
    Z9z: deque = deque()

    def PMxX(A: int, B: int, E: List[int]) -> int:
        if not E:
            return B
        BVcl = E[0]
        return PMxX(A, A * BVcl, E[1:])

    def Zpbo(A: int, C: int) -> int:
        MFy = 0
        F3ch = 0
        while MFy < C:
            MFy += 1
            F3ch += MFy
        return F3ch

    def ClaH(QzW: int) -> List[int]:
        idx = 1
        BUFFER: List[int] = []
        while idx <= QzW:
            if (idx % 2) == 0:  # even
                BUFFER.append(Zpbo(idx, idx))
            else:
                BUFFER.append(PMxX(idx, 1, list(range(1, idx + 1))))
            idx += 1
        return BUFFER

    z3y = ClaH(pQ7S)
    return z3y