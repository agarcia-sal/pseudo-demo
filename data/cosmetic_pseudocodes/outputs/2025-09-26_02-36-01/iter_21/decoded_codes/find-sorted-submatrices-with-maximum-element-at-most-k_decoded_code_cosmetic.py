class Solution:
    def countSubmatrices(self, grid, k):
        A = 0
        B = len(grid)
        C = len(grid[0])
        D = 0

        def checkLimits(M):
            E = 0
            while True:
                if E >= len(M):
                    return True
                F = 0
                while F < len(M[E]):
                    if not (M[E][F] <= k):
                        return False
                    F += 1
                E += 1

        def checkOrder(M):
            G = 0
            while True:
                if G >= len(M):
                    return True
                H = 1
                while H < len(M[G]):
                    if not (M[G][H] <= M[G][H - 1]):
                        return False
                    H += 1
                G += 1

        def loopY2(y1, y2, x1, x2):
            nonlocal D
            if y2 > C - 1:
                return
            tempSub = []
            i = x1
            while i <= x2:
                rowSegment = []
                j = y1
                while j <= y2:
                    rowSegment.append(grid[i][j])
                    j += 1
                tempSub.append(rowSegment)
                i += 1
            if checkLimits(tempSub) and checkOrder(tempSub):
                D += 1
            loopY2(y1, y2 + 1, x1, x2)

        def loopX2(x1, x2, y1):
            if x2 > B - 1:
                return
            loopY2(y1, y1, x1, x2)
            loopX2(x1, x2 + 1, y1)

        def loopY1(y1, x1):
            if y1 > C - 1:
                return
            loopX2(x1, x1, y1)
            loopY1(y1 + 1, x1)

        def loopX1(x1):
            if x1 > B - 1:
                return
            loopY1(0, x1)
            loopX1(x1 + 1)

        loopX1(0)
        return D