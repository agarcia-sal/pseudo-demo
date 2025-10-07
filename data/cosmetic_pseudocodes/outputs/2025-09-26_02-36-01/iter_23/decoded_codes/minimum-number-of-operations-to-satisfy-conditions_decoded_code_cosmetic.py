class Solution:
    def minimumOperations(self, grid):
        h = len(grid)
        w = len(grid[0])
        resultCount = 0

        def checkI(idx, col):
            nonlocal resultCount
            if idx >= h - 1:
                return
            if grid[idx][col] != grid[idx + 1][col]:
                resultCount += 1
                grid[idx + 1][col] = grid[idx][col]
            checkI(idx + 1, col)

        def findReplacement(r, c):
            nonlocal resultCount
            if c >= w - 1:
                return
            if grid[r][c] == grid[r][c + 1]:
                resultCount += 1

                def tryCandidate(x):
                    if x > 9:
                        return
                    if x != grid[r][c]:
                        grid[r][c + 1] = x
                        return
                    else:
                        tryCandidate(x + 1)

                tryCandidate(0)

        def loopCols(col):
            if col >= w:
                return
            checkI(0, col)

            def innerLoopRows(r):
                if r >= h:
                    return
                findReplacement(r, col)
                innerLoopRows(r + 1)

            innerLoopRows(0)
            loopCols(col + 1)

        loopCols(0)
        return resultCount