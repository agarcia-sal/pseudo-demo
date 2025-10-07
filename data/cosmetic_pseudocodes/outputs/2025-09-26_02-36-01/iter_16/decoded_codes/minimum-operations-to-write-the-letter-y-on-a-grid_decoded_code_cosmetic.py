from collections import defaultdict

class Solution:
    def minimumOperationsToWriteY(self, grid):
        w = len(grid)
        g = w // 2
        z = set()

        k = 0
        while k <= g:
            kv = (k, k)
            z.add(kv)
            k += 1

        m = 0
        while m <= g:
            mv = (m, (w - m - 1))
            z.add(mv)
            m += 1

        s = g
        while s <= w - 1:
            sv = (s, g)
            z.add(sv)
            s += 1

        countY = defaultdict(int)
        countN = defaultdict(int)

        r = 0
        while r < w:
            c = 0
            while c < w:
                pos = (r, c)
                val = grid[r][c]
                if pos in z:
                    countY[val] += 1
                else:
                    countN[val] += 1
                c += 1
            r += 1

        maxVal = int(1e9)
        x = 0
        while x <= 2:
            y = 0
            while y <= 2:
                if x != y:
                    sumY = 0
                    for key, v in countY.items():
                        sumY += 0 if key == x else v

                    sumN = 0
                    for key, v2 in countN.items():
                        sumN += 0 if key == y else v2

                    totalOps = sumY + sumN
                    if totalOps < maxVal:
                        maxVal = totalOps
                y += 1
            x += 1

        return maxVal