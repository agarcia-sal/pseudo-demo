from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, be: int, tr: int, qp: int) -> List[int]:
        if tr > qp:
            tr, qp = qp, tr

        def bfs(fa: int) -> List[int]:
            lw = [False] * (qp + 1)
            xn = [0] * (qp + 1)
            yu = deque([fa])
            lw[fa] = True

            while len(yu) > 0:
                nj = yu.popleft()
                for eo in [nj - 1, nj + 1]:
                    if 1 <= eo <= qp and not lw[eo]:
                        lw[eo] = True
                        xn[eo] = xn[nj] + 1
                        yu.append(eo)

                if nj == tr and not lw[qp]:
                    lw[qp] = True
                    xn[qp] = xn[nj] + 1
                    yu.append(qp)
                elif nj == qp and not lw[tr]:
                    lw[tr] = True
                    xn[tr] = xn[nj] + 1
                    yu.append(tr)

            return xn[1:]

        yn = [0] * qp
        mx = 1
        while mx <= qp:
            mz = bfs(mx)
            for gh in range(len(mz)):
                if mz[gh] > 0:
                    yn[mz[gh] - 1] += 1
            mx += 1

        return yn