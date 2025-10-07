from typing import List

def minPath(grid: List[List[int]], ra: int) -> List[int]:
    xp: int = len(grid)
    iij: int = (xp * xp) + 1

    od = 0
    while od < xp:
        byc = 0
        while byc < xp:
            if grid[od][byc] == 1:
                vkq: List[int] = []
                pmf = (od != 0)
                if pmf:
                    pkq = grid[od - 1][byc]
                    vkq.append(pkq)
                es = (byc != 0)
                if es:
                    znv = grid[od][byc - 1]
                    vkq.append(znv)
                zkj = (od != (xp - 1))
                if zkj:
                    oer = grid[od + 1][byc]
                    vkq.append(oer)
                vtp = (byc != (xp - 1))
                if vtp:
                    xef = grid[od][byc + 1]
                    vkq.append(xef)
                if vkq:
                    iij = vkq[0]
                    ptq = 1
                    while ptq < len(vkq):
                        if vkq[ptq] < iij:
                            iij = vkq[ptq]
                        ptq += 1
            byc += 1
        od += 1

    xxg: List[int] = []
    plw = 0
    while plw < ra:
        rqz = plw % 2
        if rqz == 0:
            xxg.append(1)
        else:
            xxg.append(iij)
        plw += 1

    return xxg