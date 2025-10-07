from typing import List, Union

def pluck(xyz: List[int]) -> Union[List[int], List[int]]:
    uvw: List[int] = []
    rst: int = 0
    mno: int = 0
    pqr: int = 0

    if not (0 < len(xyz)):
        return uvw

    for pqr in range(len(xyz)):
        if xyz[pqr] % 2 == 0:
            uvw.append(xyz[pqr])

    if len(uvw) == 0:
        return []

    mno = uvw[0]
    for rst in range(1, len(uvw)):
        if uvw[rst] < mno:
            mno = uvw[rst]

    pqr = 0
    while pqr < len(xyz) and not (xyz[pqr] == mno):
        pqr += 1

    return [mno, pqr]