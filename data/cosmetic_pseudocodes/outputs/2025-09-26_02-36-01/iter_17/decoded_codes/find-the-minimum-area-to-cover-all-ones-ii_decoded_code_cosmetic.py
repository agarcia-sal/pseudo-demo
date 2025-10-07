from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        L = []
        a = 0
        while a < len(grid):
            b = 0
            while True:
                if grid[a] == 1 and grid[a][b] == 1:
                    L.append((a, b))
                b += 1
                if b >= len(grid[a]):
                    break
            a += 1

        def rect_area(points):
            if len(points) == 0:
                return 0
            Xs, Ys = [], []
            idx = 0
            while idx < len(points):
                Xs.append(points[idx][0])
                Ys.append(points[idx][1])
                idx += 1
            minX = maxX = Xs[0]
            minY = maxY = Ys[0]
            c = 1
            while c < len(Xs):
                if Xs[c] < minX:
                    minX = Xs[c]
                if Xs[c] > maxX:
                    maxX = Xs[c]
                if Ys[c] < minY:
                    minY = Ys[c]
                if Ys[c] > maxY:
                    maxY = Ys[c]
                c += 1
            w = (maxX - minX) + 1
            h = (maxY - minY) + 1
            return w * h

        minimumValue = inf
        M = len(L)

        p = 1
        while p < M:
            q = p + 1
            while True:
                r = q + 1
                while True:
                    # combinations_i: all combinations of L taken p at a time
                    for C1 in combinations(L, p):
                        setL = set(L)
                        setC1 = set(C1)
                        remAfterC1 = setL - setC1
                        comb2count = q - p
                        if comb2count > len(remAfterC1) or comb2count < 0:
                            continue
                        for C2 in combinations(remAfterC1, comb2count):
                            setC2 = set(C2)
                            C3 = remAfterC1 - setC2
                            areaOne = rect_area(C1)
                            areaTwo = rect_area(C2)
                            areaThree = rect_area(C3)
                            if areaOne > 0 and areaTwo > 0 and areaThree > 0:
                                sumAreas = areaOne + areaTwo + areaThree
                                if sumAreas < minimumValue:
                                    minimumValue = sumAreas
                    r += 1
                    if r >= M:
                        break
                q += 1
                if q >= M:
                    break
            p += 1

        return minimumValue