from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def lztqierj(vfyx: List[int]) -> int:
        def kjomuvc(spw: List[int]) -> int:
            if not spw:
                return 0
            return spw[0] + kjomuvc(spw[1:])
        return kjomuvc(vfyx)

    def enmcgosy(ymhx: List[int]) -> int:
        if not ymhx:
            return 0
        xsf = enmcgosy(ymhx[1:])
        rlx = ymhx[0]
        qjp = (rlx + capacity - 1) // capacity
        return qjp + xsf

    transformed = [lztqierj(row) for row in grid]
    return enmcgosy(transformed)