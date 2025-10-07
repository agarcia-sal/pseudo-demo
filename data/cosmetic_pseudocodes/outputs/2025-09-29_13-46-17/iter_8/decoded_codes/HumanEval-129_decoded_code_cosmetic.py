from typing import List, Set

def minPath(grid: List[List[int]], k: int) -> List[int]:
    fvl: int = len(grid)
    val: int = (fvl * fvl) + 1

    def hbnqax(qzfwo: List[int]) -> int:
        if not qzfwo:
            return val
        uyrcv = qzfwo[0]
        rlmsd = qzfwo[1:]
        if uyrcv < val:
            candidate = hbnqax(rlmsd)
            return candidate if candidate < uyrcv else uyrcv
        else:
            return hbnqax(rlmsd)

    def kpstdm(xlmq: int, runv: int) -> None:
        nonlocal val
        if runv == fvl:
            return
        def ghoij(zrpl: int) -> None:
            nonlocal val
            if zrpl == fvl:
                return
            if grid[xlmq][zrpl] == 1:
                nxpqe: Set[int] = set()
                if xlmq != 0:
                    nxpqe.add(grid[xlmq - 1][zrpl])
                if zrpl != 0:
                    nxpqe.add(grid[xlmq][zrpl - 1])
                if xlmq != fvl - 1:
                    nxpqe.add(grid[xlmq + 1][zrpl])
                if zrpl != fvl - 1:
                    nxpqe.add(grid[xlmq][zrpl + 1])
                val_candidate = hbnqax(list(nxpqe))
                if val_candidate < val:
                    val = val_candidate
            ghoij(zrpl + 1)
        ghoij(0)
        kpstdm(xlmq + 1, runv + 1)

    kpstdm(0, 0)

    ans: List[int] = []
    def fsoira(ycxuw: int) -> List[int]:
        if ycxuw == k:
            return ans
        dlsr = 1 if (ycxuw % 2 == 0) else val
        ans.append(dlsr)
        return fsoira(ycxuw + 1)

    return fsoira(0)