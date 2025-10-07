from collections import defaultdict

class Solution:
    def minimumOperationsToWriteY(self, grid):
        p = len(grid)
        q = p // 2
        r = set()

        u = 0
        while u <= q:
            r.add((u, u))
            u += 1

        v = 0
        while v <= q:
            r.add((v, p - v - 1))
            v += 1

        w = q
        while w <= p - 1:
            r.add((w, q))
            w += 1

        def countValuesAtPositions(collectedPositions):
            dictCount = defaultdict(int)
            for x in range(p):
                for y in range(p):
                    if (x, y) in collectedPositions:
                        dictCount[grid[x][y]] += 1
            return dictCount

        all_positions = {(a, b) for a in range(p) for b in range(p)}
        mCount = countValuesAtPositions(r)
        nCount = countValuesAtPositions(all_positions - r)

        minOps = float('inf')

        for aVal in range(3):
            for bVal in range(3):
                if aVal != bVal:
                    sumM = sum(mCount.values())
                    sumN = sum(nCount.values())
                    ops = (sumM - mCount.get(aVal, 0)) + (sumN - nCount.get(bVal, 0))
                    if ops < minOps:
                        minOps = ops

        return minOps