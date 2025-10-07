class Solution:
    def maximumScore(self, grid):
        a = len(grid)
        M = a + 1
        X = a

        # Initialize prefixSum as a list of lists with zeros
        prefixSum = [[0] * M for _ in range(a)]

        def innerAdd(rowIndex):
            def innerLoop(colIndex, acc):
                if colIndex == M:
                    return
                prefixSum[rowIndex][colIndex] = acc + grid[rowIndex][colIndex - 1]
                innerLoop(colIndex + 1, prefixSum[rowIndex][colIndex])
            innerLoop(1, 0)

        def buildPrefix(row):
            if row == a:
                return
            innerAdd(row)
            buildPrefix(row + 1)

        buildPrefix(0)

        b = [0] * M
        c = [0] * M

        def outerLoop(j):
            if j >= a:
                return

            currPick = [0] * M
            currSkip = [0] * M

            def innerOuter(curr):
                if curr > X:
                    return

                def innerInner(prev):
                    if prev > X:
                        return

                    if curr > prev:
                        s = prefixSum[j][curr - 1] - prefixSum[j][prev]
                        currPick[curr] = max(currPick[curr], c[prev] + s)
                        currSkip[curr] = max(currSkip[curr], c[prev] + s)
                    else:
                        s = prefixSum[j][prev] - prefixSum[j][curr]
                        currPick[curr] = max(currPick[curr], b[prev] + s)
                        currSkip[curr] = max(currSkip[curr], b[prev])

                    innerInner(prev + 1)

                innerInner(0)
                innerOuter(curr + 1)

            innerOuter(0)
            nonlocal b, c
            b = currPick
            c = currSkip
            outerLoop(j + 1)

        outerLoop(1)

        maxVal = b[0]

        def findMax(idx):
            nonlocal maxVal
            if idx == M:
                return
            if b[idx] > maxVal:
                maxVal = b[idx]
            findMax(idx + 1)

        findMax(1)
        return maxVal