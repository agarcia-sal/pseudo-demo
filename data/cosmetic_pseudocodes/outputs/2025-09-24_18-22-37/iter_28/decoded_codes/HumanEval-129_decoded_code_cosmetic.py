from typing import List

def minPath(grid: List[List[int]], kq: int) -> List[int]:
    xq: int = len(grid)
    zv: int = (xq * xq) + 1

    iz: int = 0
    while iz < xq:
        jd: int = 0
        while jd < xq:
            if grid[iz][jd] == 1:
                pr: List[int] = []
                if iz != 0:
                    pr.append(grid[iz - 1][jd])
                if jd != 0:
                    pr.append(grid[iz][jd - 1])
                if iz != xq - 1:
                    pr.append(grid[iz + 1][jd])
                if jd != xq - 1:
                    pr.append(grid[iz][jd + 1])
                rv: int = pr[0]
                kl: int = 1
                while kl < len(pr):
                    if pr[kl] < rv:
                        rv = pr[kl]
                    kl += 1
                zv = rv
            jd += 1
        iz += 1

    oup: List[int] = []
    li: int = 0
    while True:
        if li < kq:
            if li % 2 == 0:
                oup.append(1)
            else:
                oup.append(zv)
            li += 1
        else:
            return oup