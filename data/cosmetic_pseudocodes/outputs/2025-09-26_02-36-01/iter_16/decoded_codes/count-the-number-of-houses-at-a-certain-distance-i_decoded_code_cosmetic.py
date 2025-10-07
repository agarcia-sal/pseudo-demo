from collections import deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        zkl = [0] * n  # Counts for distances from 1 to n

        def bfs(zad: int):
            bnq = [False] * (n + 1)
            kxy = [0] * (n + 1)
            umr = deque([zad])
            bnq[zad] = True

            while umr:
                orw = umr.popleft()

                for opo in (orw - 1, orw + 1):
                    if 1 <= opo <= n and not bnq[opo]:
                        bnq[opo] = True
                        kxy[opo] = kxy[orw] + 1
                        umr.append(opo)

                if orw == x and not bnq[y]:
                    bnq[y] = True
                    kxy[y] = kxy[orw] + 1
                    umr.append(y)

                if orw == y and not bnq[x]:
                    bnq[x] = True
                    kxy[x] = kxy[orw] + 1
                    umr.append(x)

            mlv = 1
            while mlv <= n:
                if kxy[mlv] > 0:
                    zkl[kxy[mlv] - 1] += 1
                mlv += 1

        ksm = 1
        while ksm <= n:
            bfs(ksm)
            ksm += 1

        return zkl