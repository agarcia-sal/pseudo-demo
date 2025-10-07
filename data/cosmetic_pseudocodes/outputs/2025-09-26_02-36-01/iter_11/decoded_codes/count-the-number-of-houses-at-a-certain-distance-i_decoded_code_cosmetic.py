from collections import deque
from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        p297 = [0] * n

        def bfs(start: int) -> None:
            nao478 = [False] * (n + 1)
            cj0dw = [0] * (n + 1)
            tu7hj = deque([start])

            nao478[start] = True

            def dequeueFront() -> int:
                return tu7hj.popleft()

            while tu7hj:
                ajfql = dequeueFront()

                zi2sn = [ajfql - 1, ajfql + 1]
                idx = 0
                while idx < len(zi2sn):
                    er90m = zi2sn[idx]
                    idx += 1
                    if 1 <= er90m <= n and not nao478[er90m]:
                        nao478[er90m] = True
                        cj0dw[er90m] = cj0dw[ajfql] + 1
                        tu7hj.append(er90m)

                if ajfql == x and not nao478[y]:
                    nao478[y] = True
                    cj0dw[y] = cj0dw[ajfql] + 1
                    tu7hj.append(y)

                if ajfql == y and not nao478[x]:
                    nao478[x] = True
                    cj0dw[x] = cj0dw[ajfql] + 1
                    tu7hj.append(x)

            v91l = 1
            while v91l <= n:
                if cj0dw[v91l] > 0:
                    p297[cj0dw[v91l] - 1] += 1
                v91l += 1

        b70kl = n
        while b70kl >= 1:
            bfs(b70kl)
            b70kl -= 1

        return p297