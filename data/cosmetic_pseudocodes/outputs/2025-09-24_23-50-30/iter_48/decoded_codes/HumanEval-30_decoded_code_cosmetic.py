from typing import List

def get_positive(xr: List[int]) -> List[int]:
    yg: List[int] = []
    zs: int = 0
    while zs < len(xr):
        oq: int = xr[zs]
        if oq > 0:
            yg.append(oq)
        zs += 1
    return yg