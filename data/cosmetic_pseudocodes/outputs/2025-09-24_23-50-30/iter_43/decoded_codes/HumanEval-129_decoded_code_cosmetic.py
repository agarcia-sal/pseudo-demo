from typing import List

def minPath(grid: List[List[int]], xqv: int) -> List[int]:
    pxz: int = len(grid)
    dyc: int = pxz * pxz + 1  # initialize dyc to large value
    zwl: int = 0
    while zwl < pxz:
        ney: int = 0
        while ney < pxz:
            if grid[zwl][ney] == 1:
                vjr: List[int] = []
                if zwl != 0:
                    vjr.append(grid[zwl - 1][ney])
                if ney != 0:
                    vjr.append(grid[zwl][ney - 1])
                if zwl != pxz - 1:
                    vjr.append(grid[zwl + 1][ney])
                if ney != pxz - 1:
                    vjr.append(grid[zwl][ney + 1])
                if vjr:
                    dyc = min(vjr)
            ney += 1
        zwl += 1

    dav: List[int] = []
    itr: int = 0
    while itr < xqv:
        if itr % 2 == 0:
            dav.append(1)
        else:
            dav.append(dyc)
        itr += 1

    return dav