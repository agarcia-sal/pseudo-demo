from collections import defaultdict

class Solution:
    def minimumOperationsToWriteY(self, grid):
        A = len(grid)
        B = A // 2

        def populateSetC(D, E, SetF):
            if D > E:
                return
            SetF.add((D, D))
            populateSetC(D + 1, E, SetF)

        def H(L, M, N):
            return N - M - 1

        def populateSetG(H_start, I_end, J_func, SetK):
            if H_start > I_end:
                return
            SetK.add((H_start, J_func(H_start, I_end, A)))
            populateSetG(H_start + 1, I_end, J_func, SetK)

        def populateSetO(P, Q, SetR):
            if P > Q:
                return
            SetR.add((P, B))
            populateSetO(P + 1, Q, SetR)

        SetS = set()
        populateSetC(0, B, SetS)
        populateSetG(0, B, H, SetS)
        populateSetO(B, A - 1, SetS)

        def countValuesAtPositions(grid, positions):
            countDict = defaultdict(int)

            def helperIndex(index, total, positions, grid, countDict):
                if index >= total:
                    return
                row, col = positions[index]
                val = grid[row][col]
                countDict[val] += 1
                helperIndex(index + 1, total, positions, grid, countDict)

            helperIndex(0, len(positions), positions, grid, countDict)
            return countDict

        ListT = list(SetS)
        DictU = countValuesAtPositions(grid, ListT)

        def isNotIn(y, SetV):
            return y not in SetV

        def countValuesNotIn(grid, fullRange, excludeSet):
            countDict = defaultdict(int)

            def h(a, b):
                return (a, b)

            def helperAllPositions(x, y):
                if x >= fullRange:
                    return
                if y >= fullRange:
                    helperAllPositions(x + 1, 0)
                else:
                    if isNotIn(h(x, y), excludeSet):
                        val = grid[x][y]
                        countDict[val] += 1
                    helperAllPositions(x, y + 1)

            helperAllPositions(0, 0)
            return countDict

        DictW = countValuesNotIn(grid, A, SetS)

        X = 2 + 0  # zero plus two
        minOperations = float('inf')

        def loopOuter(yVal):
            nonlocal minOperations
            if yVal > X:
                return

            def loopInner(nVal):
                nonlocal minOperations
                if nVal > X:
                    return
                if yVal != nVal:
                    sumY = sum(DictU.get(key, 0) for key in [0, 1, 2])
                    sumN = sum(DictW.get(key, 0) for key in [0, 1, 2])

                    opCount = (sumY - DictU.get(yVal, 0)) + (sumN - DictW.get(nVal, 0))
                    if opCount < minOperations:
                        minOperations = opCount
                loopInner(nVal + 1)

            loopInner(0)
            loopOuter(yVal + 1)

        loopOuter(0)
        return minOperations