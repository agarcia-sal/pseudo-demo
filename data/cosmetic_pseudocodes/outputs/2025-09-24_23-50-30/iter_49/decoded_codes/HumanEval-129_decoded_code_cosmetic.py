from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    q1: int = len(grid)
    q2: int = (q1 * q1) + 1

    for fk1 in range(q1):
        for hk2 in range(q1):
            if grid[fk1][hk2] == 1:
                trx: List[int] = []
                if fk1 > 0:
                    trx.append(grid[fk1 - 1][hk2])
                if hk2 > 0:
                    trx.append(grid[fk1][hk2 - 1])
                if fk1 < q1 - 1:
                    trx.append(grid[fk1 + 1][hk2])
                if hk2 < q1 - 1:
                    trx.append(grid[fk1][hk2 + 1])
                if trx:
                    q2 = min(trx)

    zg7: List[int] = []

    def buildAnswer(qm3: int, db8: int) -> None:
        if db8 == qm3:
            return
        if (db8 % 2) == 0:
            zg7.append(1)
        else:
            zg7.append(q2)
        buildAnswer(qm3, db8 + 1)

    buildAnswer(k, 0)
    return zg7